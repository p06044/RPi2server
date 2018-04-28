#!/usr/bin/python
#coding: utf-8
print "Content-type: text/html"
import cgi
import cgifunc
cgifunc.head('mercari')
form = cgi.FieldStorage()
tokumei = form.getvalue('tokumei','')
yahoo = form.getvalue('yahoo','')
tateyoko = form.getvalue('tateyoko','')
takasa = form.getvalue('takasa','')
sum = form.getvalue('sum','')
weight = form.getvalue('weight','')
print "匿名:"+tokumei+"<br>yahoo:"+yahoo+"<br>縦横:"+tateyoko+"<br>高さ:"+takasa+"<br>合計:"+sum+"<br>重量:"+weight
cgifunc.end()
