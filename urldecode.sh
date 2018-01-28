#!/bin/sh

echo `ruby -r cgi -e "puts CGI.unescape(\""$1"\")"`
