#!/usr/bin/python
#coding: utf-8
import sys
import io
import cgi
import sqlfunc
import cgifunc

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
cgifunc.head('application')
print "<meta http-equiv=\"refresh\" content=\"0;URL=http://p06044.server-on.net/auction.py\">"
#<!DOCTYPE html>
#<html lang="ja">
form = cgi.FieldStorage()
name = form["name"].value
#name = form.getvalue("name")
#name = cgi.escape(str(form.getvalue("name")))
#name = form.getfirst('name','none')
print name
cgifunc.end()
sqlfunc.additem(name)
