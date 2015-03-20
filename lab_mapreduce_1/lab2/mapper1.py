#!/usr/local/bin/python3

import sys

doc_count = 0
for linr in sys.stdin:
	doc_count += 1

print(doc_count)
