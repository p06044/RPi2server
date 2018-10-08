#!/bin/bash
nowD=`date "+%s"`
calc () {
	birthD=`date -d $1 '+%s'`
	ret=`expr "$birthD" - "$nowD"`
	ret=`expr $ret / 86400 + 1`
	echo "<div>$2まで<span style="color:blue">$ret</span>日！</div>"
}

cat timediff.txt | while read line
do
	calc `echo $line | awk '{print $1}'` `echo $line | awk '{print $2}'`
done
