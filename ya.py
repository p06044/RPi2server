#!/usr/bin/python
import datetime
#coding: utf-8
print "Content-type: text/html\n";
print "<HTML>"
print "<head>"
print "<meta charset=\"UTF-8\" >"
print "<title>yahoo auction list</title>"
print "</head>"
print "<body>"
print "<body>"

#ページリンクパート
print "<a href=\"amazonlist.html\">[ama]</a><a href=\"cron.html\">[cron]</a><a href=\"auctionlist.html\">[meru]</a><span style=\"color:orange;\">[yauc]</span><a href=\"timer.html\">[timer]</a><a href=\"phpbutton.html\">[button]</a><a href=\"tumblr.html\">[tumblr]</a>"
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

#ヤフオクリンク
print "<a href=\"https://auctions.yahoo.co.jp/search/search?p=kals+%E8%A6%81%E9%A0%85%E9%9B%86&auccat=0&fixed=0\" target=\"_blank\">ヤフオク</a>"

#ヤフオクパート三重大
#wget -O yalist.html "https://auctions.yahoo.co.jp/rss?p=%E4%B8%89%E9%87%8D%E5%A4%A7%E5%AD%A6&ei=UTF-8&oq=&auccat=2084008618&slider=0&fixed=0&s1=cbids&o1=a" &
#wait $!
#NAMES=($(cat yalist.html| sed -e "/ヤフオク/d" | grep -A1 title | grep title | sed -e "s/^.*<title>\(.*\)<\/title>.*$/\1/" -e "s/ //g" -e "s/　//g"))
#PRICES=($(cat yalist.html| grep 現在価格 | sed -e "s/^.*現在価格:\(.*\)円.*$/\1/" -e "s/,//g"))
#LINK=($(cat yalist.html | sed "/\/\/auctions/d" | grep \<link\> | sed -e "s/^.*<link>\(.*\)<\/link>.*$/\1/"))
#i=0
#j=`expr ${#NAMES[@]}`
#while [ $i -ne $j ]
#do
#	if [ `echo ${NAMES[$i]} | grep '2015' | grep '三重' | grep -v '看護' | grep -v 'AO' ` ] ; then
#		echo "<div><span style=\"color:red;\">${NAMES[$i]}</span><a href=\"${LINK[$i]}\" target=\"_blank\">${PRICES[$i]}</a></div>" >> /home/pi/ya.html
#	elif [ `echo ${NAMES[$i]} | grep '三重' | grep -e '2013' -e '2014' -e '2016' -e '2017' | grep -v '看護' | grep -v 'AO' ` ] ; then
#		echo "<div><span style=\"color:orange;\">${NAMES[$i]}</span><a href=\"${LINK[$i]}\" target=\"_blank\">${PRICES[$i]}</a></div>" >> /home/pi/ya.html
#	else
#		echo "<div><span style=\"color:black;\">${NAMES[$i]}</span><a href=\"${LINK[$i]}\" target=\"_blank\">${PRICES[$i]}</a></div>" >> /home/pi/ya.html
#	fi
#	i=`expr $i + 1`
#done

#ヤフオクパート要項集
wget -O yalist.html "https://auctions.yahoo.co.jp/rss?p=kals+%E8%A6%81%E9%A0%85%E9%9B%86&oq=&auccat=0&fixed=0&ei=UTF8" &
wait $!
NAMES=($(cat yalist.html| sed -e "/ヤフオク/d" | grep -A1 title | grep title | sed -e "s/^.*<title>\(.*\)<\/title>.*$/\1/" -e "s/ //g" -e "s/　//g"))
PRICES=($(cat yalist.html| grep 現在価格 | sed -e "s/^.*現在価格:\(.*\)円.*$/\1/" -e "s/,//g"))
LINK=($(cat yalist.html | sed "/\/\/auctions/d" | grep \<link\> | sed -e "s/^.*<link>\(.*\)<\/link>.*$/\1/"))
i=0
j=`expr ${#NAMES[@]}`
while [ $i -ne $j ]
do
	echo "<div><span style=\"color:black;\">${NAMES[$i]}</span><a href=\"${LINK[$i]}\" target=\"_blank\">${PRICES[$i]}</a></div>" >> /home/pi/ya.html
	i=`expr $i + 1`
done

mv /home/pi/ya.html /var/www/html
