#!/usr/bin/python

import subprocess

def res_cmd_lfeed(cmd):
	return subprocess.Popen(
		cmd, stdout=subprocess.PIPE,
		shell=True).stdout.readlines()

def res_cmd_no_lfeed(cmd):
	return [str(x).rstrip("\n") for x in res_cmd_lfeed(cmd)]

def main():
	cmd = ("ls -tl /home/pi/share")
	result = res_cmd_no_lfeed(cmd)
	del result[0]
	for l in range(len(result)):
		line = result[l]
		word = line.split()
		print('<div>%s %s %s %s</div>' % (word[5], word[6],word[7],word[8]))

if __name__ == '__main__':
	main()
