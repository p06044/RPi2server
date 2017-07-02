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
echo "<a href=\"amazonlist.html\">[ama]</a><span style=\"color:orange;\">[cron]</span><a href=\"auctionlist.html\">[auc]</a><a href=\"ya.html\">[yauc]</a>" >> /home/pi/cron.html
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

echo "</body>
</html>" >> /home/pi/cron.html

mv cron.html /var/www/html

