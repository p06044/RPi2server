#!/bin/sh
echo "<html>
<head>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" >
    <meta charset=\"UTF-8\" >
    <title>amazon list</title>
</head>
<body>
    <SCRIPT LANGUAGE=\"JavaScript\">
        setTimeout(\"location.reload()\",1000*3600);
    </SCRIPT>" >> /home/pi/cron.html

echo `date` >> /home/pi/cron.html
#crontab -l >> cron.html
crontab -l | while read line
do
        echo "<div>${line}</div>" >> /home/pi/cron.html
done

echo "</body>
</html>" >> /home/pi/cron.html

mv cron.html /var/www/html

