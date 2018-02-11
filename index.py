#!/usr/bin/python
#coding:utf-8
import afi
import head
import link

#head
head.main()
#apache
f = open('/home/pi/gittxt/index.html')
areas = f.read().splitlines()
for line in areas:
	print line
f.close()

#afi
afi.main()
#link
link.main('index')
#end
head.end()
