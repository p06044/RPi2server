#!/usr/bin/python
#coding:utf-8
import datetime
import commands
import link
import afi

print "Content-type: text/html\n"
print "<html>"
print "<head>"
print "    <meta charset=\"UTF-8\">"
print "    <title>schedule</title>"
print "</head>"
print "<body>"

#page link
link.links('cron')

#date
date = datetime.date.today()
print date 

#afi
afi.afi()

#date countdown
check = commands.getoutput("bash /home/pi/git/timediff.sh")
print check 

#samba
samba = commands.getoutput("ls -tl /home/pi/share | tail -n +2 | awk \'{print $6,$7,$8,$9}\'")
print "<div>"+samba+"</div>"

#weight
print "<div><img src=\"weight.png\" width=\"30%\"></div>"

#CRON
f = open('crontab.txt')
areas = f.read().splitlines()
for line in areas:
	print "<div>"+line+"</div>"

print "</body>"
print "</html>"
