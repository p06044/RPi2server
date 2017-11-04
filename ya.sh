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
echo "<a href=\"amazonlist.html\">[ama]</a><a href=\"cron.html\">[cron]</a><a href=\"auctionlist.html\">[meru]</a><span style=\"color:orange;\">[yauc]</span>" >> /home/pi/ya.html
RET='\
'

#アフィパート
echo "<script async src=\"//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\"></script>
<!-- ふゎーおすまほ -->
<ins class=\"adsbygoogle\"
     style=\"display:inline-block;width:300px;height:250px\"
     data-ad-client=\"ca-pub-8948717586645505\"
     data-ad-slot=\"2135626673\"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</body>
</html>" >> /home/pi/ya.html

#ヤフオクリンク
echo "<a href=\"https://auctions.yahoo.co.jp/search/search?p=kals+%E8%A6%81%E9%A0%85%E9%9B%86&auccat=0&fixed=0\" target=\"_blank\">ヤフオク</a>" >> /home/pi/ya.html

#ヤフオクパート三重大
wget -O yalist.html "https://auctions.yahoo.co.jp/rss?p=%E4%B8%89%E9%87%8D%E5%A4%A7%E5%AD%A6&ei=UTF-8&oq=&auccat=2084008618&slider=0&fixed=0&s1=cbids&o1=a" &
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
