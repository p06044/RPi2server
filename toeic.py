#!/usr/bin/python
#coding:utf-8
import requests
import sys
import datetime

date = datetime.date.today()
outf = '/home/pi/share/'+str(date)+'.html'
print outf
url = 'https://www.iibc-global.org/toeic/test/lr/about/pr.html'
res = requests.get(url)
with open(outf, 'w') as file:
    file.write(res.text.encode('utf-8'))
