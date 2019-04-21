#!/usr/bin/python
#coding:utf-8
import cgi
import cgifunc
import flashsqlfunc

cgifunc.head('deleteword')
print "<meta http-equiv=\"refresh\" content=\"0;URL=http://p06044.server-on.net/flashcard.py\">"
form = cgi.FieldStorage()
id = form["btn"].value
print id
cgifunc.end()
flashsqlfunc.delete(id)
