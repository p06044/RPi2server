#!/usr/bin/python
#coding: utf-8
import link
import afi

print "Content-type: text/html\n"
print "<HTML>"
print "<head>"
print "<meta charset=\"UTF-8\" >"
print "<title>tumblr tag</title>"
print "</head>"
print "<body>"
link.links('tumblr')
print "<br/>"

f = open('tumblrS.txt')
areas = f.read().splitlines()
for line in areas:
	print "<a href=\"http://sortme.tumblr.com/tagged/"+line.split()[0]+"\" target=\"_blank\">"+line.split()[1]+"</a>"
f.close()

f = open('tumblrG.txt')
areas = f.read().splitlines()
for line in areas:
	print "<a href=\"http://gravua.tumblr.com/tagged/"+line.split()[0]+"\" target=\"_blank\">"+line.split()[1]+"</a>"
f.close()

afi.afi()
print "</body>"
print "</HTML>"
