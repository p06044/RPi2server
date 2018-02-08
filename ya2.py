#!/usr/bin/python
#coding:utf-8
import requests
import datetime
import commands
import link
import afi
import head
from bs4 import BeautifulSoup

head.main()
link.links('ya')
date = datetime.date.today()
print date 
afi.main()

url = "https://auctions.yahoo.co.jp/search/search?p=kals+%E8%A6%81%E9%A0%85%E9%9B%86"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html5lib")

#title = []
#for tag in soup.find_all("h3"):
#	title.append(tag.get_text())

price = []
for tag in soup.find_all(class_="pr1"):
	tag.ul.extract()
	text = tag.get_text().replace("\n","").replace(" ","")
	price.append(text)

link = []
for tag in soup.find_all("h3"):
	tag.find("href")
	link.append(tag)

for line in range(len(link)):
#	print('%s, %s' % (link[line], price[line]))
	print('%s' % link[line])
	print('%s" % price[line])

head.end()
