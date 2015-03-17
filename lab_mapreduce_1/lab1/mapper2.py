#!/usr/local/bin/python3

import sys
import json

for line in sys.stdin:
	doc = json.loads(line)
	topics = doc['topics']
	for topic in topics:
		print(topic)
