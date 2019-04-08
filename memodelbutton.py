#!/usr/bin/python
#coding:utf-8
import cgi
import cgifunc
import memosqlfunc

cgifunc.head('deleteline')
print "<meta http-equiv=\"refresh\" content=\"0;URL=http://p06044.server-on.net/memopad.py\">"
form = cgi.FieldStorage()
id = form["btn"].value
print id
cgifunc.end()
memosqlfunc.delete(id)
