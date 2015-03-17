#!/usr/local/bin/python3

import sys
import json

result = {}
for line in sys.stdin:
	obj = json.loads(line)
	token = obj['token']
	body = obj['body']
	if 'idf' in body.keys():
		idf = float(body['idf'])
	else:
		idf = 0
	
	docs = body['docs']
	for hash in docs.keys():
		tf = float(docs[hash]['tf'])
		if hash in result.keys():
			result[hash]['tfidf'][token] = tf * idf
		else:
			result[hash] = {}
			result[hash]['topics'] = docs[hash]['topics']
			result[hash]['tfidf'] = {}
			result[hash]['tfidf'][token] = tf * idf
			
	
for key in result.keys():
	print(json.dumps({'hash': key, 'body': result[key]}))
