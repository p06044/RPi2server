#!/usr/bin/python
#coding:utf-8
import datetime
import commands
import cgifunc
from bs4 import BeautifulSoup

cgifunc.head('yafuoku')
cgifunc.link('yauc')
date = datetime.date.today()
print date 
cgifunc.afi()
print "<br/>"

f = open('/home/pi/gittxt/yahtml.txt')
areas = f.read().splitlines()
for line in areas:
	print line
cgifunc.end()
