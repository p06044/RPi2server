#!/usr/bin/python
#coding:utf-8
import cgi
import cgifunc
import sqlfunc

cgifunc.head('delete')
print "<meta http-equiv=\"refresh\" content=\"0;URL=http://p06044.server-on.net/auction.py\">"
form = cgi.FieldStorage()
id = form["btn"].value
print id
cgifunc.end()
sqlfunc.delete(id)
