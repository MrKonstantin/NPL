#!/usr/local/bin/python3

import sys
import json


for line in sys.stdin:
	try:
		token, idf, docs = line.strip().split('\t')
		docs = json.load(docs)

		for doc in docs:
			print(doc['id'], doc['topics'], token, idf * doc['tf'], sep='\t')
	except:
		pass
