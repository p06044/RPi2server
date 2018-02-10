#!/usr/bin/python
#coding: utf-8
import link
import afi
import urlencode
import head

head.main()
link.main('tumblr')
print "<br/>"

f = open('tumblr.txt')
areas = f.read().splitlines()
for line in areas:
	word = urlencode.main(line)
	print "<a href=\""+line+"\" target=\"_blank\">"+word+"</a>"
f.close()

afi.main()
head.end()
