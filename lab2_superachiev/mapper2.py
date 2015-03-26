#!/usr/local/bin/python3

from sys import stdin

for line in stdin:
	url, count = line.strip().split('\t')
	print(str(count) + '\t' + url)
