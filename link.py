#!/usr/bin/python
#coding: utf-8
link = [['ama', 'amazonlist.html'], ['cron', 'cronhtml.py'], ['meru', 'auctionlist.html'], ['yauc', 'ya2.py'], ['timer', 'timer.html'], ['button', 'phpbutton.html'], ['tumblr', 'tumblr.py']]

def links(this):
	for a in range(len(link)):
		if link[a][0] == this:
			print "<span style=\"color:orange;\">["+link[a][0]+"]</span>"
		else:
			print "<a href="+link[a][1]+">["+link[a][0]+"]</a>"
