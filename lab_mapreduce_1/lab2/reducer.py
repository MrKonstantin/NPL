#!/usr/local/bin/python3

import sys
import math

result = {}
docs_total = 0

first = None

for line in sys.stdin:
	token, count, d_count = line.strip().split(".....")
	if token in result.keys():
		result[token] += int(float(count))
	else:
		result[token] = int(float(count))
		if first == None:
			first = token

	if first == token:
		docs_total += int(float(d_count))

for token in result.keys():
	print(token, math.log(docs_total/result[token]))
