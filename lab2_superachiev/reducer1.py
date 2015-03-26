#!/usr/local/bin/python3

from sys import stdin

prev = None
count = 0
for line in stdin:
	url = line.strip().split('\n')[0]
	if prev is None:
		count = 1
		prev = url
	elif prev != url:
		print(url, count, sep='\t')
		count = 1
		prev = url
	else:
		count += 1
