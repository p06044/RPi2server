#!/usr/bin/python
#coding:utf-8
import datetime
import commands
import cgifunc

cgifunc.head('cron')

#page link
cgifunc.link('cron')

#date
date = datetime.date.today()
print date 

#afi
cgifunc.afi()

#date countdown
check = commands.getoutput("bash /home/pi/git/timediff.sh")
print check 

#samba
#samba = commands.getoutput("ls -tl /home/pi/share | tail -n +2 | awk \'{print $6,$7,$8,$9}\'")
#print "<div>"+samba+"</div>"
cgifunc.ls()

#weight
print "<div><img src=\"weight.png\" width=\"50%\"></div>"

#CRON
f = open('crontab.txt')
areas = f.read().splitlines()
for line in areas:
	print "<div>"+line+"</div>"

cgifunc.end()
