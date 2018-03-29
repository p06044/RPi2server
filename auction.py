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

word = ['要項集 KALS', 'ライジング古文', 'みんなが欲しかった! 社労士の問題集 2018']

for a in range(len(word)):
	#print cgifunc.amalink(word[a])+" "+cgifunc.merulink(word[a])+" "+cgifunc.yaholink(word[a])+"<br/>"
	print cgifunc.link3(word[a])+"<br/>"
cgifunc.end()
