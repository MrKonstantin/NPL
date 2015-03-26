#!/usr/local/bin/python3

from sys import stdin

n = 0
for line in stdin:
	n += 1
	if n <= 350:
		count, url = line.strip().split('\t')
		print(url, count, sep='\t')
	else:
		break
