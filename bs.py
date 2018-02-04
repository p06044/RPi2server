#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
url = "https://auctions.yahoo.co.jp/search/search?p=kals+%E8%A6%81%E9%A0%85%E9%9B%86"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html5lib")

#print soup.prettify()
print soup.find(class_="pr1")
print soup.find(class_="a1wrp")
