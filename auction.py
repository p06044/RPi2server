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
print "<a href=\"http://fuwaao.blogspot.com/search/label/%E3%83%A1%E3%83%AB%E3%82%AB%E3%83%AA%E5%87%BA%E5%93%81%E4%B8%80%E8%A6%A7\" target=\"_blank\">出品リスト</a><br/>"

f = open('auction.txt')
areas = f.read().splitlines()
for a in areas:
	print cgifunc.link3(a)
f.close()
cgifunc.end()
