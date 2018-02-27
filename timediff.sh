#!/bin/bash
nowD=`date "+%s"`
#簿記
birthD=`date -d "20180610" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>簿記まで<span style="color:blue">$ret</span>日！</div>"
#宅建
birthD=`date -d "20181021" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>宅建まで<span style="color:blue">$ret</span>日！</div>"
