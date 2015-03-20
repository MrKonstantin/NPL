#!/usr/local/bin/python3
import sys

total_doc = 0
for line in sys.stdin:
	total_doc += int(float(line))

print(total_doc)
