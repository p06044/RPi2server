#!/usr/bin/python
#coding:utf-8
import datetime
import cgifunc

cgifunc.head('meru')
cgifunc.link('meru')
date = datetime.date.today()
print date 
cgifunc.afi()
print "<br/>"
url = ['https://www.mercari.com/jp/search/?sort_order=price_asc&keyword=KALS%E3%80%80%E8%A6%81%E9%A0%85&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=&status_on_sale=1', 'https://www.mercari.com/jp/search/?sort_order=price_asc&keyword=%E3%83%A9%E3%82%A4%E3%82%B8%E3%83%B3%E3%82%B0%E5%8F%A4%E6%96%87&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=&status_on_sale=1', 'https://www.mercari.com/jp/search/?sort_order=&keyword=%E3%81%BF%E3%82%93%E3%81%AA%E3%81%8C%E6%AC%B2%E3%81%97%E3%81%8B%E3%81%A3%E3%81%9F%21+%E7%A4%BE%E5%8A%B4%E5%A3%AB%E3%81%AE%E5%95%8F%E9%A1%8C%E9%9B%86+2018&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=&status_on_sale=1']


for a in range(len(url)):
	print "<a href=\""+url[a]+"\">"+cgifunc.encomeru(url[a])+"</a><br/>"
cgifunc.end()
