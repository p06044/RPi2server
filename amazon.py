#!/usr/bin/python
#coding:utf-8
import datetime
import cgifunc

cgifunc.head('amazon')
cgifunc.link('amazon')
date = datetime.date.today()
print date 
cgifunc.afi()
print "<br/>"

f = open('/home/pi/gittxt/amazonhtml.txt')
areas = f.read().splitlines()
for line in areas:
	print line
cgifunc.end()
