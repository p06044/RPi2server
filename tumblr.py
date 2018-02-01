#!/usr/bin/python
#coding: utf-8
print "Content-type: text/html\n";
print "<HTML>"
print "<head>"
print "<meta charset=\"UTF-8\" >"
print "<title>tumblr tag</title>"
print "</head>"
print "<body>"
print "<a href=\"amazonlist.html\">[ama]</a><a href=\"cron.html\">[cron]</a><a href=\"auctionlist.html\">[meru]</a><a href=\"ya.html\">[yauc]</a><a href=\"timer.html\">[timer]</a><a href=\"phpbutton.html\">[button]</a><span style=\"color:orange;\">[tumblr]</span>"
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

print "<script async src=\"//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\"></script>"
print "<!-- ふゎーおすまほ -->"
print "<ins class=\"adsbygoogle\""
print "     style=\"display:inline-block;width:300px;height:250px\""
print "     data-ad-client=\"ca-pub-8948717586645505\""
print "     data-ad-slot=\"2135626673\"></ins>"
print "<script>"
print "(adsbygoogle = window.adsbygoogle || []).push({});"
print "</script>"
print ""
print "</body>"
print ""
print "</HTML>"
