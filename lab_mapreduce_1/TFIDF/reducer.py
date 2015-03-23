#!/usr/local/bin/python3

import sys
import json

result = {}

for line in sys.stdin:
	split = line.strip().split('-----')
	token = split[0]
	if token not in result.keys():
		result[token] = {}

	if len(split) == 2:
		idf = split[1]
		result[token]['idf'] = idf
	else:
		doc = {}
		hash = split[1]
		doc['tf'] = split[2]
		doc['topics'] = split[3]
		
		if 'docs' in result[token]:
			result[token]['docs'][hash] = doc
		else:
			result[token]['docs'] = {}
			result[token]['docs'][hash] = doc

for token in result.keys():
	print(json.dumps({'token': token, 'body': result[token]}))

