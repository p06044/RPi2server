#!/bin/sh

echo `ruby -r cgi -e "puts CGI.escape(\""$1"\")"`
