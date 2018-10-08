#!/bin/bash

cat timediff.txt | while read line
do
	echo $line | awk '{print $1}'
done
