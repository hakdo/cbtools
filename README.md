# cbtools
This is just a dumping ground for small tools, typically for cybersecurity. 

# License: 
Use as you wish, for what you wish. No guarantees, support given, no liability accepted. Use at your own risk. v

## phishtime.py
Search for a URL in the History file from Microsoft Edge. The History file is a sqlite3 database and can normally be found at: 

`C:\Users\<username>\AppData\Local\Microsoft\Edge\User Data\Default\History`

Usage: `./phishtime.py <History> <url> 1`. 

This seaches for an exact match in the history database. If you want to search for a URL fragment, use `./phishtime.py <History> <url-fragment> 2`  instead.

Output: a simple table of timestamps for *last visit* and the URL visited: 

```
----------------------------------------------------------------
Matches found in browser history for search term _vg.no_
----------------------------------------------------------------

Last visited         URL
-------------------  ------------------
2023-10-13 19:06:03  http://www.vg.no/
2023-10-18 09:36:52  https://www.vg.no/

Browser history search complated at: 2023-10-18 12:28:17.335597
```