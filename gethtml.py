#!/usr/bin/python
#coding:utf-8
import requests
import sys
#url = "https://auctions.yahoo.co.jp/search/search?p=kals+%E8%A6%81%E9%A0%85%E9%9B%86"
#url = 'https://www.iibc-global.org/toeic/test/lr/about/pr.html'
res = requests.get(sys.argv[1])
with open(sys.argv[2], 'w') as file:
    file.write(res.text.encode('utf-8'))
