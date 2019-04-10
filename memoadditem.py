#!/usr/bin/python
#coding: utf-8
#import sys
#import io
import cgi
import memosqlfunc
import cgifunc

cgifunc.head('add')
print "<meta http-equiv=\"refresh\" content=\"0;URL=http://p06044.server-on.net/memopad.py\">"
form = cgi.FieldStorage()
name = form["name"].value.replace('\'', '\'\'')
print name
cgifunc.end()
memosqlfunc.additem(name)
