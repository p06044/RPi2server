#!/usr/bin/python
#coding:utf-8
import datetime
import commands
import link
import afi
import ls
import head
#import clist

head.main()

#page link
link.main('cron')

#date
date = datetime.date.today()
print date 

#afi
afi.main()

#date countdown
check = commands.getoutput("bash /home/pi/git/timediff.sh")
print check 

#samba
#samba = commands.getoutput("ls -tl /home/pi/share | tail -n +2 | awk \'{print $6,$7,$8,$9}\'")
#print "<div>"+samba+"</div>"
ls.main()

#weight
print "<div><img src=\"weight.png\" width=\"30%\"></div>"

#CRON
#clist.main()
f = open('crontab.txt')
areas = f.read().splitlines()
for line in areas:
	print "<div>"+line+"</div>"

head.end()
