#!/usr/bin/python
#coding:utf-8
import datetime
import commands

print "Content-type: text/html\n"
print "<html>"
print "<head>"
print "    <meta charset=\"UTF-8\">"
print "    <title>schedule</title>"
print "</head>"
print "<body>"

#page link
print "<a href=\"amazonlist.html\">[ama]</a><span style=\"color:orange;\">[cron]</span><a href=\"auctionlist.html\">[meru]</a><a href=\"ya.html\">[yauc]</a><a href=\"timer.html\">[timer]</a><a href=\"phpbutton.html\">[button]</a><a href=\"tumblr.html\">[tumblr]</a>"

#date
date = datetime.date.today()
print date 

#afi
print "<script async src=\"//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\"></script>"
print "<!-- ふゎーおすまほ -->"
print "<ins class=\"adsbygoogle\""
print "     style=\"display:inline-block;width:300px;height:250px\""
print "     data-ad-client=\"ca-pub-8948717586645505\""
print "     data-ad-slot=\"2135626673\"></ins>"
print "<script>"
print "(adsbygoogle = window.adsbygoogle || []).push({});"
print "</script>"

#date countdown
check = commands.getoutput("bash /home/pi/git/timediff.sh")
print check 

#samba
samba = commands.getoutput("ls -tl /home/pi/share | tail -n +2 | awk \'{print $6,$7,$8,$9}\'")
print "<div>"+samba+"</div>"

#weight
print "<div><img src=\"/home/pi/weight.png\" width=\"30%\"></div>"

#CRON
f = open('crontab.txt')
areas = f.read().splitlines()
for line in areas:
	print "<div>"+line+"</div>"

print "</body>"
print "</html>"
