#!/usr/bin/python
#coding:utf-8
import datetime
import cgifunc
import requests
from bs4 import BeautifulSoup

def main():
	url = "https://www.amazon.co.jp/gp/registry/wishlist/AIL114CMM7OU/ref=nav_wishlist_lists_4"
	html = requests.get(url)
	soup = BeautifulSoup(html.text, "html5lib")

	link = []
	for tag in soup.find_all('h5'):
		a = tag.find('a')
		link.append(a)
	del link[len(link)-1]

	price = []
	for tag in soup.find_all(class_="a-color-price itemUsedAndNewPrice"):
		price.append(tag)

	f = open('/home/pi/gittxt/amazonhtml.txt', 'w')
	for line in range(len(price)):
		f.write('%s <span style=\"color:orange;\">%s</span><br/>' % (link[line].encode('utf-8'),price[line].encode('utf-8')))
	f.close()

if __name__ == '__main__':
	main()
