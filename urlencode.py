#!/usr/bin/python

import urllib

def main(url):
	tag=  url.split("/")
	parse = urllib.unquote(tag[4])
	return parse

if __name__ == '__main__':
	main()
