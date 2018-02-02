#!/usr/bin/python
import datetime
import commands

#coding: utf-8
print "Content-type: text/html\n";
print "<html>"
print "<head>"
print "    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" >"
print "    <meta charset=\"UTF-8\" >"
print "    <title>schedule</title>"
print "</head>"
print "<body>"

#ページリンクパート
print "<a href=\"amazonlist.html\">[ama]</a><span style=\"color:orange;\">[cron]</span><a href=\"auctionlist.html\">[meru]</a><a href=\"ya.html\">[yauc]</a><a href=\"timer.html\">[timer]</a><a href=\"phpbutton.html\">[button]</a><a href=\"tumblr.html\">[tumblr]</a>"

#日付パート
date = datetime.date.today()
print(date)

#アフィパート
print "<script async src=\"//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\"></script>"
print "<!-- ふゎーおすまほ -->"
print "<ins class=\"adsbygoogle\""
print "     style=\"display:inline-block;width:300px;height:250px\""
print "     data-ad-client=\"ca-pub-8948717586645505\""
print "     data-ad-slot=\"2135626673\"></ins>"
print "<script>"
print "(adsbygoogle = window.adsbygoogle || []).push({});"
print "</script>"

#センターカウントダウン
check = commands.getoutput("bash /homepi/git/timediff.sh")
print check

#sambaパート
ls -tl share | tail -n +2 | awk '{print $6,$7,$8,$9}' | while read line
do
	echo "<div>${line}</div>" >> /home/pi/cron.html
done

samba = commands.getoutput("ls -tl share | tail -n +2 | awk \'{print $6,$7,$8,$9}\'"

#体重パート
print "<div><img src=\"/home/pi/weight.png\" width=\"30%\"></div>"

#CRONパート
cronl = commands.getoutput("crontab -l")
areas = cronl.read().splitlines()
print areas

print "</body>"
print "</html>"
