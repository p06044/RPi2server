#!/usr/bin/python
#coding:utf-8
import requests
import datetime
import commands
import link
import afi
import head
from bs4 import BeautifulSoup

head.main()
link.main('ya')
date = datetime.date.today()
print date 
afi.main()
print "<br/>"

f = open('/home/pi/gittxt/yahtml.txt')
areas = f.read().splitlines()
for line in areas:
	print line
head.end()
