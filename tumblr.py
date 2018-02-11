#!/usr/bin/python
#coding: utf-8
import urlencode
import cgifunc

cgifunc.head()
cgifunc.link('tumblr')
print "<br/>"

f = open('tumblr.txt')
areas = f.read().splitlines()
for line in areas:
	word = cgifunc.urlencode(line)
	print "<a href=\""+line+"\" target=\"_blank\">"+word+"</a>"
f.close()

cgifunc.afi()
cgifunc.end()
