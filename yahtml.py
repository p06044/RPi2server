#!/usr/bin/python
#coding:utf-8
import requests
from bs4 import BeautifulSoup

def main():
	url = "https://auctions.yahoo.co.jp/search/search?p=%E8%A9%B3%E8%A7%A3+%E7%A4%BE%E4%BC%9A%E7%A6%8F%E7%A5%89%E5%A3%AB+%E9%81%8E%E5%8E%BB+%E5%95%8F%E9%A1%8C%E9%9B%86+18%E5%B9%B4"
	html = requests.get(url)
	soup = BeautifulSoup(html.text, "html5lib")

	price = []
	for tag in soup.find_all(class_="pr1"):
		tag.ul.extract()
		text = tag.get_text().replace("\n","").replace(" ","")
		price.append(text)

	link = []
	for tag in soup.find_all('h3'):
		a = tag.find('a')
		link.append(a)

	f = open('/home/pi/gittxt/yahtml.txt', 'w')
	for line in range(len(link)):
		f.write('%s <span style=\"color:orange;\">%s</span><br/>' % (link[line].encode('utf-8'), price[line].encode('utf-8')))
	f.close()

if __name__ == '__main__':
	main()
