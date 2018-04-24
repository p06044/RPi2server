#!/usr/bin/python
#coding:utf-8
import requests
from bs4 import BeautifulSoup

def main():
	url = "https://auctions.yahoo.co.jp/search/search?p=%E3%82%88%E3%81%8F%E3%82%8F%E3%81%8B%E3%82%8B%E7%A4%BE%E5%8A%B4%E5%A3%AB+2018"
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
