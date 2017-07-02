#!/bin/sh
echo "<html>
<head>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" >
    <meta charset=\"UTF-8\" >
    <title>amazon list</title>
</head>
<body>
    <SCRIPT LANGUAGE=\"JavaScript\">
        setTimeout(\"location.reload()\",1000*60);
    </SCRIPT>" >> /home/pi/amazonlist.html

#日付パート
echo `date` >> /home/pi/amazonlist.html

#ページリンクパート
echo "<a href=\"http://p06044.server-on.net/ya.html\">[yauc]</a><a href=\"http://p06044.server-on.net/cron.html\">[cron]</a><a href=\"http://p06044.server-on.net/auctionlist.html\">[auc]</a>" >> /home/pi/amazonlist.html
RET='\
'

#アマゾンパート
for j in `cat wlist.html | grep pag-trigger | sed -e "s/^.*quot;:\(.*\)\}\".*$/\1/"`
do
    wget -O wlist.html "https://www.amazon.co.jp/gp/registry/wishlist/AIL114CMM7OU/ref=cm_wl_sortbar_o_page_${j}?ie=UTF8&page=${j}" &
    wait $!
    NAMES=($(cat wlist.html | grep -A 1 -e "a id=\"itemName" | grep -v "a id=\"itemName" | sed -e "s/--//g" -e "s/ //g" | grep -v '^\s*$'))
    PRICES=($(cat wlist.html | grep "￥" | grep "より" | sed -e "s/<span class=\"a-color-price itemUsedAndNewPrice\">//g" -e "s/<\/span>より//g" -e "s/￥ //g" -e "s/ //g" -e "s/,//g"))
    LINK=($(cat wlist.html | grep "a id=\"itemName" | sed -e "s/<a id=\"itemName.*href=\"\/dp\/\(.*\)?_encoding.*$/\1/" -e "s/ //g"))
#文字色設定
    i=0
    j=`expr ${#NAMES[@]}`
    while [ $i -ne $j ]
    do
        if [ ${PRICES[$i]} -gt 1000 ] ; then
            col="black"
        elif [ ${PRICES[$i]} -gt 100 ] ; then
            col="orange"
        else
            col="red"
        fi
#文字列出力
        echo "<div><span style=\"color:${col};\">${NAMES[$i]}</span><a href=\"https:\/\/www.amazon.co.jp\/gp\/offer-listing\/${LINK[$i]}\" target=\"_blank\">${PRICES[$i]}</a></div>" >> /home/pi/amazonlist.html
        i=`expr $i + 1`
    done
done

echo "</body>
</html>" >> /home/pi/amazonlist.html

mv /home/pi/amazonlist.html /var/www/html
