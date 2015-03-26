#!/usr/local/bin/python3

from sys import stdin

count = 0
for line in stdin:
	count += 1
	if count <= 350:
		count, url = line.strip().split('\t')
		print(url, count, sep='\t')
	else:
		break