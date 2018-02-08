#!/usr/bin/python
#coding: utf-8
import link
import afi
import urlencode

print "Content-type: text/html\n"
print "<HTML>"
print "<head>"
print "<meta charset=\"UTF-8\" >"
print "<title>tumblr tag</title>"
print "</head>"
print "<body>"
link.main('tumblr')
print "<br/>"

f = open('tumblr.txt')
areas = f.read().splitlines()
for line in areas:
	word = urlencode.main(line)
	print "<a href=\""+line+"\" target=\"_blank\">"+word+"</a>"
f.close()

afi.main()
print "</body>"
print "</HTML>"
