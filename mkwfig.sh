#!/bin/bash

A=/var/www/html/weight.png
B=/home/pi/share/統計記録.xls
if [ $A -ot $B ]; then
	python /home/pi/weight.py
fi
