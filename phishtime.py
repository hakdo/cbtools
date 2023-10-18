import sys, sqlite3

"""
This script expects you to provide it a Chrome/Chromium/Edge History file as input, 
as well as a URL you would like to check against the history. 

The URL can be checked for 
1 - Exact match
2 - LIKE match

hakdo-at-outlook-dot-com 2023
"""
import tabulate
from datetime import datetime as dt

database = sys.argv[1]
target = sys.argv[2]
matchtype = int(sys.argv[3])


db = sqlite3.connect(database)
cursor = db.cursor()

def query_generator(matcher):
    if matcher == 1:
        query = "SELECT datetime(last_visit_time/1000000 + (strftime('%s','1601-01-01')),'unixepoch','localtime'), url FROM urls where url=?;"
    elif matcher == 2:
        query = "SELECT datetime(last_visit_time/1000000 + (strftime('%s','1601-01-01')),'unixepoch','localtime'), url FROM urls where url like '%'||?||'%';"
    else:
        raise Exception("Invalid query selector number - you can only choose (1) Excact or (2) LIKE.")
    return query

try:
    query = query_generator(matchtype)
except Exception as e:
    print("Error - : ", e)

res = cursor.execute(query,(target,))
out = res.fetchall()
print()
print('--------------------------------------------------------------------------')
print("Matches found in browser history for search term _%s_" % target)
print('--------------------------------------------------------------------------')
print()
print(tabulate.tabulate(out,headers=['Last visited', 'URL']))
print()
print('Browser history search complated at: ' + str(dt.now()))