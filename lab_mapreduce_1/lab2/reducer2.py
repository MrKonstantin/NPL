#!/usr/local/bin/python3

import sys
import math

prev_token = None
token_count = 0

f = open('AllDocCount', 'r')
all_doc_count = float(f.readline())

for line in sys.stdin:
	token, value = line.strip().split('\t')
	value = int(float(value))
	if token == prev_token:
		token_count += value
	else:
		print(token, math.log(all_doc_count/token_count))
		prev_token = token
		token_count = value