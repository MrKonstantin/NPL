#!/usr/local/bin/python3

import sys
import json

prev = {'token': None, 'idf': 0, 'docs': []}

for line in sys.stdin:
	split = line.strip().split('\t')
	token = split[0]

	if prev['token'] is None:
		prev = {'token': token, 'idf': 0, 'docs': []}
	elif token != prev['token']:
		print(prev['token'], prev['idf'], json.dumps(prev['docs']), sep='\t')
		prev = {'token': token, 'idf': 0, 'docs': []}

	if len(split) == 2:
		idf = split[1]
		prev['idf'] = idf
	else:
		doc = {'id': split[1], 'tf': split[2], 'topics': split[3]}
		prev['docs'].append(doc)

if prev['token'] is not None:
	print(prev['token'], prev['idf'], json.dumps(prev['docs']), sep='\t')