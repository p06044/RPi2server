#!/bin/sh

if [ $1 = "encode" ]; then
	echo `ruby -r cgi -e "puts CGI.escape(\""$2"\")"`
elif [ $1 = "decode" ]; then
	echo `ruby -r cgi -e "puts CGI.unescape(\""$2"\")"`
fi
