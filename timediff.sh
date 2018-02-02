#!/bin/bash
nowD=`date "+%s"`
birthD=`date -d "20180225" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>二次試験まで<span style="color:blue">$ret</span>日！</div>"
#echo "<div>二次試験まで<span style="color:blue">$ret</span>日！</div>" >> /home/pi/cron.html
