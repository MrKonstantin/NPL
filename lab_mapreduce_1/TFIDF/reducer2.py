#!/usr/local/bin/python3

import sys
import json

prev = {'id': None}

for line in sys.stdin:

		doc_id, topics, token, tfidf = line.strip().split('\t')
		if prev['id'] is None:
			prev = {'id': doc_id, 'topics': topics, 'tokens':{token: tfidf}}
		elif prev['id'] != doc_id:
			print({'topics': prev['topics'], 'tokens': prev['tokens']})
			prev = {'id': doc_id, 'topics': topics, 'tokens':{token: tfidf}}
		else:
			prev['tokens'][token] = tfidf
