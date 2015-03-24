#!/usr/local/bin/python3

import sys
import json


for line in sys.stdin:
	token, idf, docs_str = line.strip().split('\t')
	docs = json.loads(docs_str)

	for doc in docs:
		print(doc['id'], doc['topics'], token, float(idf) * float(doc['tf']), sep='\t')