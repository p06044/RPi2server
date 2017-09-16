#!/bin/bash

A=/var/www/html/weight.png
B=/home/pi/share/統計記録.xls
if [ $A -ot $B ]; then
	python weight.py
else
	echo `date` > ${HOME}/share/weight.log
	echo "no update" >> ${HOME}/share/weight.log
fi
