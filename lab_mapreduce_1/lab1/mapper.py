#!/usr/local/bin/python3

import sys
import json


def _map(key, value):
	doc = json.loads(value)
	topics = doc['topics']
	for topic in topics:
		print(topic)

for line in sys.stdin:
	_map(None, line)
