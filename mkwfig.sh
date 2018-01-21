#!/bin/bash

A=/var/www/html/weight.png
B=/home/pi/share/統計記録.xls
CMD=/home/pi/weight-transition/weight.py
if [ -e $A ]; then
	if [ $A -ot $B ]; then
		python $CMD
	fi
else
	python $CMD
fi
