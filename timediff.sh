#!/bin/bash
nowD=`date "+%s"`
#birthD=`date -d "20180826" '+%s'`
#ret=`expr "$birthD" - "$nowD"`
#ret=`expr $ret / 86400 + 1`
#echo "<div>社労士まで<span style="color:blue">$ret</span>日！</div>"
birthD=`date -d "20181007" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>電工まで<span style="color:blue">$ret</span>日！</div>"
birthD=`date -d "20181020" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>ボイラーまで<span style="color:blue">$ret</span>日！</div>"
birthD=`date -d "20181111" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>行書まで<span style="color:blue">$ret</span>日！</div>"
birthD=`date -d "20190119" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>センターまで<span style="color:blue">$ret</span>日！</div>"
birthD=`date -d "20190204" '+%s'`
ret=`expr "$birthD" - "$nowD"`
ret=`expr $ret / 86400 + 1`
echo "<div>社福まで<span style="color:blue">$ret</span>日！</div>"

