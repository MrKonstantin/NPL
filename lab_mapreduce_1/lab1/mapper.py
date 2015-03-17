#!/usr/local/bin/python3
import json
import sys

result = {}
for line in sys.stdin:
    doc = json.loads(line)
    topics = doc['topics']

    for topic in topics:
        if topic in result.keys():
            result[topic] += 1
        else:
            result[topic] = 1

for topic in result.keys():
    print(topic, result[topic], sep = ".....")
