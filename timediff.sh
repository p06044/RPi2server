#!/bin/bash
nowD=`date "+%s"`
birthD=`date -d "20180113" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div><span style="color:blue">センターまで$ret日！</span></div>" >> /home/pi/cron.html
