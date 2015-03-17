#!/usr/local/bin/python3

import sys
import json

result = {}
docs_count = 0

for line in sys.stdin:
	doc = json.loads(line)
	tokens = set(doc['tokens'])
	for token in tokens:
		if token in result.keys():
			result[token] += 1
		else:
			result[token] = 1
	docs_count += 1

for key in result.keys():
	print(key, result[key], docs_count, sep = ".....")	

	
