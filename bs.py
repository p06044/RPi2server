#!/usr/bin/python
#coding:utf-8
import requests
from bs4 import BeautifulSoup
url = "https://auctions.yahoo.co.jp/search/search?p=kals+%E8%A6%81%E9%A0%85%E9%9B%86"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html5lib")

#print soup.prettify()
title = []
for tag in soup.find_all("h3"):
	title.append(tag.get_text())

price = []
for tag in soup.find_all(class_="pr1"):
	tag.ul.extract()
	text = tag.get_text().replace("\n","").replace(" ","")
	price.append(text)

link = []
for tag in soup.find_all("h3"):
	tag.find("h3")
	print tag

#for line in range(len(title)):
#	print('%s, %s' % (title[line], price[line]))
