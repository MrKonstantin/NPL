#!/usr/local/bin/python3

import sys
import json

prev = None

for line in sys.stdin:
	try:
		split = line.strip().split('\t')
		token = split[0]

		if token is not None and token != prev['token'] and isinstance(prev, dict):
			print(prev['token'], prev['idf'], json.dumps(prev['docs']), sep='\t')
			prev = {'token': token, 'idf': 0, 'docs': []}

		if token is None:
			prev = {'token': token, 'idf': 0, 'docs': []}

		if len(split) == 2:
			idf = split[1]
			prev['body']['idf'] = idf
		else:
			doc = {}
			doc['id']= split[1]
			doc['tf'] = split[2]
			doc['topics'] = split[3]

			prev['docs'].add(doc)

	except:
		pass
