#!/usr/bin/python
#coding:utf-8
import requests
import sys
url = 'https://www.iibc-global.org/toeic/test/lr/about/pr.html'
res = requests.get(url)
with open('/home/pi/share/toeic.html, 'w') as file:
    file.write(res.text.encode('utf-8'))
