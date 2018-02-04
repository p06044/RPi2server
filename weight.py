# -*- coding: utf-8 -*-
import xlrd
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def weight():
	book = xlrd.open_workbook('/home/pi/share/統計記録.xls')
	sheet = book.sheet_by_index(1)
	nrows = sheet.nrows
	data = np.zeros(2*nrows).reshape((nrows,2))
	date = []
	for col in [0, 1]:
		for row in range(sheet.nrows):
			if col==0:
				d =  xlrd.xldate.xldate_as_datetime(sheet.cell(row,col).value, book.datemode)
				date.append(d)
			data[row,col] = sheet.cell(row,col).value
	weight = data[:,1]
	plt.xticks(rotation =12)
	plt.plot(date, weight, label=date[nrows-1])
	plt.grid()
	plt.legend()
	plt.savefig("/home/pi/git/weight.png")

def main():
	A = '/home/pi/git/weight.png'
	B = '/home/pi/share/統計記録.xls'
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
