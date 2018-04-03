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
#	['meru', 'auctionlist.html'], 
	['meru', 'auction.py'], 
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
	tag =  url.split("/")
	parse = urllib.unquote(tag[4])
	return parse

def link3(word):
	decode = urllib.quote(word)
	aurl = 'https://www.amazon.co.jp/s/url=search-alias%3Daps&field-keywords='+decode
	murl = 'https://www.mercari.com/jp/search/?sort_order=price_asc&keyword='+decode+'&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=&shipping_payer_id%5B2%5D=1&status_on_sale=1'
	yurl = 'https://auctions.yahoo.co.jp/search/search?p='+decode+'&ei=UTF-8&s1=cbids&o1=a'
	burl = 'http://www.bookoffonline.co.jp/display/L001,st=u,bg=12,q='+decode
	rurl = 'https://search.rakuten.co.jp/search/event/'+decode+'/200162/?ev=19&evsitem=%E3%80%90%E4%B8%AD%E5%8F%A4%E3%80%91&s=2'
	link = '<div><a href=\"'+murl+'\" target=\"_blank\">[m]</a> <a href=\"'+aurl+'\" target=\"_blank\">[a]</a> <a href=\"'+yurl+'\" target=\"_blank\">[y]</a> <a href=\"'+burl+'\" target=\"_blank\">[b]</a> <a href=\"'+rurl+'\" target=\"_blank\">[r]</a>'+word+'</div>'
	return link

#if __name__ == '__main__':
#	main()
