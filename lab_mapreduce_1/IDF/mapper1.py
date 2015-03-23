#!/usr/local/bin/python3

import sys

# Считаем количество документов на каждой ноде
doc_count = 0
for linr in sys.stdin:
	doc_count += 1

print(doc_count)
