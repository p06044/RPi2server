#!/usr/bin/python
#coding:utf-8
import datetime
import cgifunc
import sqlfunc

cgifunc.head('meru')
cgifunc.link('meru')
date = datetime.date.today()
print date 
cgifunc.afi()
print "<br/>"
print "<a href=\"http://fuwaao.blogspot.com/search/label/%E3%83%A1%E3%83%AB%E3%82%AB%E3%83%AA%E5%87%BA%E5%93%81%E4%B8%80%E8%A6%A7\" target=\"_blank\">出品リスト</a><br/>"

print "<form method=\"POST\" action=\"additem.py\">"
print "<p>商品名：<input type=\"text\" name=\"name\"><input type=\"submit\" value=\"追加\"></p>"
print "</form>"

#f = open('auction.txt')
#areas = f.read().splitlines()
#for a in areas:
#	print cgifunc.link3(a)
#f.close()

for i in range(0,sqlfunc.recordcount()):
    name = sqlfunc.selectbycount(i)[1].encode('utf-8')
    print cgifunc.link3(name)
cgifunc.end()
