#!/bin/sh

lines=`curl -s "https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX" | grep -o '<dd id="USDJPY_.*</dd></dl>' | sed -e "/.*open.*/d" -e "/.*high.*/d" -e "/.*change.*/d" -e "/.*low.*/d" -e "s/^.*<dd id.*>\(.*\)<span class=\"large\">\(.*\)<\/span>\(.*\)<\/dd><\/dl>.*$/\1\2\3/"`
Bid=`echo $lines | awk '{print $1}'`
Ask=`echo $lines | awk '{print $2}'`
echo `date +"%Y%m%d%H%M%S"`, $Bid, $Ask >> fx.csv
tail -n 720 fx.csv > tfx.csv
mv tfx.csv fx.csv

