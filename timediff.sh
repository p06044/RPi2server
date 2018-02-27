#!/bin/bash
nowD=`date "+%s"`
birthD=`date -d "20180610" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>簿記まで<span style="color:blue">$ret</span>日！</div>"
