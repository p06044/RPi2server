#!/usr/bin/python
#coding: utf-8
import cgifunc

cgifunc.head('tumblr')
cgifunc.link('tumblr')
print "<br/>"
print "<a href=\"https://lab.syncer.jp/Tool/Webp-Converter/\" target=\"_blank\">webp</a><br/><a href=\"https://convertio.co/ja/image-converter/\" target=\"_blank\">webp2</a><br/><a href=\"https://www.tumblr.com/dashboard\" target=\"_blank\">tumblr</a>"
f = open('tumblr.txt')
areas = f.read().splitlines()
for line in areas:
	word = cgifunc.urlencode(line)
	#print "<a href=\""+line+"\" target=\"_blank\">"+word+"</a>"
f.close()

cgifunc.afi()
cgifunc.end()
