#!/usr/bin/python
#coding:utf-8
import datetime
import cgifunc

cgifunc.head('meru')
cgifunc.link('meru')
date = datetime.date.today()
print date 
cgifunc.afi()
print "<br/>"

f = open('auction.txt')
areas = f.read().splitlines()
for a in areas:
	print cgifunc.link3(a)
f.close()
cgifunc.end()
