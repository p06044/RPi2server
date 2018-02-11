#!/usr/bin/python
#coding: utf-8
import subprocess
import urllib

def afi():
	print "<script async src=\"//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\"></script>"
	print "<!-- ふゎーおすまほ -->"
	print "<ins class=\"adsbygoogle\""
	print "     style=\"display:inline-block;width:300px;height:250px\""
	print "     data-ad-client=\"ca-pub-8948717586645505\""
	print "     data-ad-slot=\"2135626673\"></ins>"
	print "<script>"
	print "(adsbygoogle = window.adsbygoogle || []).push({});"
	print "</script>"

def head(title):
	print "Content-type: text/html\n"
	print "<html>"
	print "<head>"
	print "    <meta charset=\"UTF-8\">"
	print "    <title>"+title+"</title>"
	print "</head>"
	print "<body>"

def end():
	print "</body>"
	print "</html>"

def link(this):
	link = [['amazon', 'amazon.py'], 
	['cron', 'cronhtml.py'], 
	['meru', 'auctionlist.html'], 
	['yauc', 'ya2.py'], 
	['timer', 'timer.html'], 
	['button', 'phpbutton.html'], 
	['tumblr', 'tumblr.py']]

	for a in range(len(link)):
		if link[a][0] == this:
			print "<span style=\"color:orange;\">["+link[a][0]+"]</span>"
		else:
			print "<a href="+link[a][1]+">["+link[a][0]+"]</a>"

def res_cmd_lfeed(cmd):
	return subprocess.Popen(
		cmd, stdout=subprocess.PIPE,
		shell=True).stdout.readlines()

def res_cmd_no_lfeed(cmd):
	return [str(x).rstrip("\n") for x in res_cmd_lfeed(cmd)]

def ls():
	cmd = ("ls -tl /home/pi/share")
	result = res_cmd_no_lfeed(cmd)
	del result[0]
	for l in range(len(result)):
		line = result[l]
		word = line.split()
		print('<div>%s %s %s %s</div>' % (word[5], word[6],word[7],word[8]))

def urlencode(url):
	tag=  url.split("/")
	parse = urllib.unquote(tag[4])
	return parse

#if __name__ == '__main__':
#	main()
