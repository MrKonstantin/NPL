#!/usr/local/bin/python3

import sys

result = {}
for line in sys.stdin:
	split = line.strip().split(', ')
	country = split[2]
	payload = split[4]
	
	if country in result.keys():
		result[country] += float(payload)
	else:
		result[country] = float(payload)

for key in result.keys():
	print(key, result[key], sep = ", ")
