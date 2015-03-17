#!/usr/local/bin/python3

import sys
import json
import hashlib

for line in sys.stdin:
	split = line.strip().split(' ')
	if len(split) == 2: #tokens
		token = split[0]
		idf = split[1]
		print(token, idf, sep = '-----')
	else: #documetns
		doc = json.loads(line)
		hash = hashlib.md5(line.encode('utf-8')).digest()
		tokens = doc['tokens']
		topics = doc['topics']
		
		all = len(tokens)
		tokens_count = {}
		for token in tokens:
			if token in tokens_count.keys():
				tokens_count[token] += 1
			else:
				tokens_count[token] = 1
			
		for token in tokens_count.keys():
			print(token, hash, tokens_count[token]/all, topics, sep = '-----')

