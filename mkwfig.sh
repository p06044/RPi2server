#!/bin/bash

A=/var/www/html/cron.html
B=/home/pi/share/統計記録.xls
if [ $A -nt $B ]; then
	python weight.py
fi
