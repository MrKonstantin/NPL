#!/usr/local/bin/python3

from sys import stdin

for line in stdin:
	uid, tmstp, url = line.strip().split('\t')
	print(url)