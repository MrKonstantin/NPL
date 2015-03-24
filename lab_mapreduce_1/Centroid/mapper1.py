#!/usr/local/bin/python3

from sys import stdin
import json

for line in stdin:
	doc = json.loads(line)
	for topic in doc['topics']:
		for token in doc['tokens'].keys():
			print(topic + ':::' + token, doc['tokens'][token], sep='\t')