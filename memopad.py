#!/usr/bin/python
#coding:utf-8
import datetime
import cgifunc
import memosqlfunc

cgifunc.head('memopad')
cgifunc.link('memopad')
date = datetime.date.today()
print date 
cgifunc.afi()
print "<br/>"

print "<form method=\"POST\" action=\"memoadditem.py\">"
print "<p>商品名：<input type=\"text\" name=\"name\" id=\"addtext\"><input type=\"submit\" class=\"btn-square-shadow\" value=\"追加\"></p>"
print "<script type=\"text/javascript\">document.getElementById('addtext').focus();</script>"
print "</form>"

memosqlfunc.link4for()
cgifunc.end()
