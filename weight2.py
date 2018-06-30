# -*- coding: utf-8 -*-
import xlrd
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def weight():
	book = xlrd.open_workbook('/home/pi/share/統計記録2.xls')
	sheet = book.sheet_by_index(1)
	nrows = sheet.nrows
	data = np.zeros(5*nrows).reshape((nrows,5))
	date = []
	for col in [0, 1, 2, 3, 4]:
		for row in range(sheet.nrows):
			if col==0:
				d =  xlrd.xldate.xldate_as_datetime(sheet.cell(row,col).value, book.datemode)
				date.append(d)
			data[row,col] = sheet.cell(row,col).value
	weight = data[:,1]
	high = data[:,2]
	low = data[:,3]
	rate = data[:,4]

	fig = plt.figure(figsize=(8, 10))

	fig.add_subplot(411)
	plt.grid()
	plt.plot(date, weight, "g", label=date[nrows-1])
	plt.legend(bbox_to_anchor=(0, 1), loc='upper left')

	fig.add_subplot(412)
	plt.grid()
	plt.plot(date, high, "r", label="high")
	plt.legend(bbox_to_anchor=(0, 1), loc='upper left')

	fig.add_subplot(413)
	plt.grid()
	plt.plot(date, low, "b", label="low")
	plt.legend(bbox_to_anchor=(0, 1), loc='upper left')

	ax = fig.add_subplot(414)
	plt.grid()
	#plt.xticks(rotation =12)
	ax.plot(date, rate, "g", label="rate")
	fig.autofmt_xdate()

	plt.legend(bbox_to_anchor=(0, 1), loc='upper left')
	plt.savefig("/home/pi/git/weight.png")

def main():
	A = '/home/pi/git/weight.png'
	B = '/home/pi/share/統計記録2.xls'
	Aexists = os.path.exists(A)
	Bexists = os.path.exists(B)
	if Bexists:
		if Aexists:
			Atime = os.stat(A).st_mtime
			Btime = os.stat(B).st_mtime
			if Atime < Btime:
				weight()
		else:
			weight()		

if __name__ == '__main__':
	main()
