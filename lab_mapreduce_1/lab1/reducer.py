#!/usr/local/bin/python3
import json
import sys

result = {}
for line in sys.stdin:
	key, val = line.strip().split(".....")
	if key in result.keys():
		result[key] += int(float(val))
	else:
		result[key] = int(float(val))

for topic in result.keys():
	print(topic, result[topic])

