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
print "<a href="https://www.amazon.co.jp/hz/wishlist/ls/3DWA0M1KJI44Z?&sort=default" target="_blank">ほしい物リスト</a><br/>"
f = open('/home/pi/gittxt/amazonhtml.txt')
areas = f.read().splitlines()
for line in areas:
	rpl = line.replace('/dp', 'https://www.amazon.co.jp/dp')
	print rpl
cgifunc.end()
