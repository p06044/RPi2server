#!/bin/sh
echo "<html>
<head>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" >
    <meta charset=\"UTF-8\" >
    <title>yahoo auction list</title>
</head>
<body>
    <SCRIPT LANGUAGE=\"JavaScript\">
        setTimeout(\"location.reload()\",1000*60);
    </SCRIPT>" >> /home/pi/ya.html

#日付パート
echo `date` >> /home/pi/ya.html

#ページリンクパート
echo "<a href=\"amazonlist.html\">[ama]</a><a href=\"cron.html\">[cron]</a><a href=\"auctionlist.html\">[auc]</a><span style="color:black;">[yauc]</span>" >> /home/pi/ya.html
RET='\
'

#ヤフオクパート
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

echo "</body>
</html>" >> /home/pi/ya.html

mv /home/pi/ya.html /var/www/html
