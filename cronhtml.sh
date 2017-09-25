#!/bin/sh
echo "<html>
<head>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" >
    <meta charset=\"UTF-8\" >
    <title>schedule</title>
</head>
<body>
    <SCRIPT LANGUAGE=\"JavaScript\">
        setTimeout(\"location.reload()\",1000*60);
    </SCRIPT>" >> /home/pi/cron.html

#日付パート
echo `date` >> /home/pi/cron.html

#ページリンクパート
echo "<a href=\"amazonlist.html\">[ama]</a><span style=\"color:orange;\">[cron]</span><a href=\"auctionlist.html\">[meru]</a><a href=\"ya.html\">[yauc]</a>" >> /home/pi/cron.html

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
</html>" >> /home/pi/cron.html

#センターカウントダウン
bash /home/pi/timediff.sh

#SAMBAパート
ls -tl share | tail -n +2 | awk '{print $6,$7,$8,$9}' | while read line
do
	echo "<div>${line}</div>" >> /home/pi/cron.html
done

#体重パート
echo "<div><img src=\"weight.png\" width=\"30%\"></div>" >> /home/pi/cron.html

#CRONパート
crontab -l | while read line
do
        echo "<div>${line}</div>" >> /home/pi/cron.html
done

mv cron.html /var/www/html

