#!/usr/bin/python
#coding:utf-8
import cgifunc

#head
cgifunc.head('apache2')
#apache
f = open('/home/pi/gittxt/index.html')
areas = f.read().splitlines()
for line in areas:
	print line
f.close()

#afi
cgifunc.afi()
#link
cgifunc.link('index')
#end
cgifunc.end()
