#!/usr/local/bin/python3

import sys
import math

prev_token = None
token_count = 0

# Загружаем количество документов
f = open('totalDoc')
all_doc_count = float(f.read())

# Расчитываем IDF для каждого токена
for line in sys.stdin:
	token, value = line.strip().split('\t')
	value = int(float(value))
	if token == prev_token:
		token_count += value
	else:
		if token_count > 0:
			print(prev_token, math.log(all_doc_count/token_count))
		prev_token = token
		token_count = value

if token_count > 0:
	print(prev_token, math.log(all_doc_count/token_count))