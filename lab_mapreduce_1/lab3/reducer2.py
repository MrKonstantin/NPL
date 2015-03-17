#!/usr/local/bin/python3

import sys
import json

result = {}

for line in sys.stdin:
	obj = json.loads(line)
	hash = obj['hash']
	body = obj['body']
	if hash in result.keys():
		for token in body['tfidf'].keys():
			result[hash]['tfidf'][token] = body['tfidf'][token]
	else:
		result[hash] = {}
		result[hash]['tfidf'] = {}
		result[hash]['topics'] = body['topics']
		for token in body['tfidf'].keys():
                        result[hash]['tfidf'][token] = body['tfidf'][token]
			
for doc in result.keys():
	print(result[doc])
