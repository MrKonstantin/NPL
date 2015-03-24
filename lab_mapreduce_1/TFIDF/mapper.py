#!/usr/local/bin/python3

import sys
import json
import hashlib

# Делаем join исходного файла с документами и файла с IDF токенов по ключу токен
# Одновременно считаем TF для каждого токена в документе
for line in sys.stdin:
	try:
		split = line.strip().split(' ')

		# Файл токенов
		if len(split) == 2:
			token = split[0]
			idf = split[1]
			print(token, idf, sep='\t')

		# Файл документов
		else:
			doc = json.loads(line)
			doc_id = hashlib.md5(line.encode('utf-8')).digest()
			tokens = doc['tokens']
			topics = doc['topics']

			# Количество токенов в документе
			tokens_number = len(tokens)
			if tokens_number == 0:
				continue

			# Токен и сколько раз он встречается в документе
			tokens_count = {}
			for token in tokens:
				if token in tokens_count.keys():
					tokens_count[token] += 1
				else:
					tokens_count[token] = 1

			for token in tokens_count.keys():
				print(token, doc_id, tokens_count[token]/tokens_number, topics, sep='\t')
	except:
		continue

