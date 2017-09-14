#!/bin/bash
nowD=`date "+%s"`
birthD=`date -d "20180113" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>センターまで<span style="color:blue">$ret</span>日！</div>" >> /home/pi/cron.html
