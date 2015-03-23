#!/usr/local/bin/python3

import sys
import json

prev = (None, [], {})

for line in sys.stdin:
	try:
		doc_id, topics, token, tfidf = line.strip().split('\t')
		if prev is None:
			prev = (doc_id, topics, {token: tfidf})
		elif prev[0] != doc_id:
			print(prev)
			prev = (doc_id, topics, {token: tfidf})
		else:
			prev[2][token] = tfidf
	except:
		pass
