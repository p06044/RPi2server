#!/bin/sh
echo "<html>
<head>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" >
    <meta charset=\"UTF-8\" >
    <title>merukari list</title>
</head>
<body>
    <SCRIPT LANGUAGE=\"JavaScript\">
        setTimeout(\"location.reload()\",1000*60);
    </SCRIPT>" >> /home/pi/auctionlist.html

#ページリンクパート
echo "<a href=\"amazonlist.html\">[ama]</a><a href=\"cron.html\">[cron]</a><span style=\"color:orange;\">[meru]</span><a href=\"ya.html\">[yauc]</a><a href=\"timer.html\">[timer]</a><a href=\"phpbutton.html\">[button]</a>" >> /home/pi/auctionlist.html
RET='\
'

echo "<br/>" >> /home/pi/auctionlist.html
#日付パート
echo `date` >> /home/pi/auctionlist.html

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
</html>" >> /home/pi/auctionlist.html

#メルカリパート三重大学
#wget -O auclist.html "https://www.mercari.com/jp/search/?sort_order=price_asc&keyword=%E4%B8%89%E9%87%8D%E5%A4%A7%E5%AD%A6&category_root=5&category_child=72&category_grand_child%5B1124%5D=1&brand_name=&brand_id=&size_group=&price_min=&price_max=&status_on_sale=1" &
#wait $!
#NAMES=($(cat auclist.html | grep items-box-name | sed -e "s/^.*<h3 class=\"items-box-name font-2\">\(.*\)<\/h3>.*$/\1/" | sed -e "s/　//g" -e "s/ //g"))
#PRICES=($(cat auclist.html | grep items-box-price | sed -e "s/^.*<div class=\"items-box-price font-5\">\(.*\)<\/div>.*$/\1/" | sed -e "s/¥ //g" -e "s/,//g"))
#LINK=($(cat auclist.html | grep -B1 "<figure class=\"items-box-photo\">" | grep href | sed -e "s/^.*<a href=\"\(.*\)\">.*$/\1/"))
#i=0
#j=`expr ${#NAMES[@]}`
#while [ $i -ne $j ]
#do
#	if [ `echo ${NAMES[$i]} | grep '2015' | grep '三重' | grep -v '看護' | grep -v 'AO' ` ] ; then
#	
#		echo "<div><span style=\"color:red;\">${NAMES[$i]}</span><a href=\"${LINK[$i]}\" target=\"_blank\">${PRICES[$i]}</a></div>" >> /home/pi/auctionlist.html
#	elif [ `echo ${NAMES[$i]} | grep '三重' | grep -e '2014' -e '2013' -e '2016' -e '2017' | grep -v '看護'| grep -v 'AO' ` ] ; then
#		echo "<div><span style=\"color:orange;\">${NAMES[$i]}</span><a href=\"${LINK[$i]}\" target=\"_blank\">${PRICES[$i]}</a></div>" >> /home/pi/auctionlist.html
#	else
#		echo "<div><span style=\"color:black;\">${NAMES[$i]}</span><a href=\"${LINK[$i]}\" target=\"_blank\">${PRICES[$i]}</a></div>" >> /home/pi/auctionlist.html
#	fi
#	i=`expr $i + 1`
#done

#メルカリパート要項集
wget -O auclist.html "https://www.mercari.com/jp/search/?sort_order=&keyword=kals+%E8%A6%81%E9%A0%85%E9%9B%86&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=&status_on_sale=1" &
wait $!
NAMES=($(cat auclist.html | grep items-box-name | sed -e "s/^.*<h3 class=\"items-box-name font-2\">\(.*\)<\/h3>.*$/\1/" | sed -e "s/　//g" -e "s/ //g"))
PRICES=($(cat auclist.html | grep items-box-price | sed -e "s/^.*<div class=\"items-box-price font-5\">\(.*\)<\/div>.*$/\1/" | sed -e "s/¥ //g" -e "s/,//g"))
LINK=($(cat auclist.html | grep -B1 "<figure class=\"items-box-photo\">" | grep href | sed -e "s/^.*<a href=\"\(.*\)\">.*$/\1/"))
i=0
j=`expr ${#NAMES[@]}`
while [ $i -ne $j ]
do
	echo "<div><span style=\"color:black;\">${NAMES[$i]}</span><a href=\"${LINK[$i]}\" target=\"_blank\">${PRICES[$i]}</a></div>" >> /home/pi/auctionlist.html
	i=`expr $i + 1`
done

mv /home/pi/auctionlist.html /var/www/html
