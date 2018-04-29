#!/usr/bin/python
#coding: utf-8
print "Content-type: text/html"
import cgi
import cgifunc
cgifunc.head('mercari')
form = cgi.FieldStorage()
tokumei = form.getvalue('tokumei','')
yahoo = form.getvalue('yahoo','')
tateyoko = form.getvalue('tateyoko','')
post = form.getvalue('post','')
takasa = form.getvalue('takasa','')
sum = form.getvalue('sum','')
weight = form.getvalue('weight','')

if tokumei == "y":
	if post == "f" or post == "y":
		if tateyoko == "1" or tateyoko == "2":
			if takasa == "1":
				print "ネコポス:195円(一律)"
			elif takasa == "2" or takasa == "3" or takasa == "4":
				print "宅急便コンパクト:380円+65円(専用資材)"
			elif takasa == "5":
				if sum == "1" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5"):
					print "宅急便60サイズ"
				elif ((sum == "1" or sum == "2") and weight == "8") or (sum == "2" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7" or weight == "8")):
					print "宅急便80サイズ"
				elif ((sum == "1" or sum == "2" or sum == "3") and weight == "9") or (sum == "3" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7" or weight == "8" or weight == "9")):
					print "宅急便100サイズ"
				elif ((sum == "1" or sum == "2" or sum == "3" or sum == "4") and weight == "10") or (sum == "4" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7" or weight == "8" or weight == "9" or weight == "10")):
					print "宅急便120サイズ"
				elif ((sum == "1" or sum == "2" or sum == "3" or sum == "4" or sum == "5") and weight == "11") or (sum == "5" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7" or weight == "8" or weight == "9" or weight == "10" or weight == "11")):
					print "宅急便140サイズ"
				elif ((sum == "1" or sum == "2" or sum == "3" or sum == "4" or sum == "5" or sum == "6") and weight == "12") or (sum == "6" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7" or weight == "8" or weight == "9" or weight == "10" or weight == "11" or weight == "12")):
					print "宅急便160サイズ"
				elif ((sum == "1" or sum == "2" or sum == "3" or sum == "4" or sum == "5" or sum == "6" or sum == "7") and weight == "13") or (sum == "6" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7" or weight == "8" or weight == "9" or weight == "10" or weight == "11" or weight == "12" or weight == "13")):
					print "大型らくらくメルカリ便"
				else:
					print "宅急便取り扱えません"
			else:
				print "高さ取り扱えません"
		else:
			print "縦横取り扱えません"
	elif post == "r":
		if tateyoko == "1" or tateyoko == "2":
			if takasa == "1":
				print "ゆうパケット:175円(一律)"
			elif sum == "1" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7" or weight == "8" or weight == "9" or weight == "10" or weight == "11" or weight == "12"):
				print "ゆうパック60サイズ"
			elif sum == "2" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7" or weight == "8" or weight == "9" or weight == "10" or weight == "11" or weight == "12"):
				print "ゆうパック80サイズ"
			elif sum == "3" and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7" or weight == "8" or weight == "9" or weight == "10" or weight == "11" or weight == "12"):
				print "ゆうパック100サイズ"
			else:
				print "取り扱えません"
		else:
			print "取り扱えません"
	elif post == "p" and yahoo == "y" and (tateyoko == "1" or tateyoko == "2") and takasa == "3" and (weight == "1" or weight == "2" or weight == "3" or weight == "4"):
		print "クリックポスト164円(一律)"
elif tokumei == "n":
	if weight == "1" or weight == "2":
		print "普通郵便定型"
	elif weight == "3":
		print "普通郵便規格内"
	elif weight == "4":
		if (tateyoko == "1" or tateyoko == "2") and (takasa == "1" or takasa == "2" or takasa == "3") and (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6"):
			print "ゆうメール"
		else:
			print "取り扱えません"
	else:
		if (tateyoko == "1" or tateyoko == "2"):
			if (weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6" or weight == "7"):
				if takasa == "1" or takasa == "2" or takasa == "3":
					print "レターパックライト360円"
				elif takasa == "4" or takasa == "5":
					print "レターパックプラス510円"
			elif weight == "8" or weight == "9" or weight == "10" or weight == "11" or weight == "12" or weight == "13":
				if sum == "7":
					print "大型らくらくメルカリ便"
				else:
					print "ヤマト宅急便"
			
cgifunc.end()
