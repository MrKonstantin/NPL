#!/usr/local/bin/python3

import sys
import json


def _map(key, doc):
	tokens = set(doc['tokens'])
	for token in tokens:
		print(token, 1, sep="\t")

for line in sys.stdin:
	_map(None, json.loads(line))