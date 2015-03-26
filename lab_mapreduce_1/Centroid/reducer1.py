#!/usr/local/bin/python3
from sys import stdin
import pandas

prev = None
num = 0
tfidf_sum = 0

for line in stdin:
	topic_token, tfidf = line.strip().split('\t')
	tfidf = float(tfidf)

	if prev is None:
		prev = topic_token
		num = 1
		tfidf_sum = tfidf
	elif prev != topic_token:
		token, topic = prev.strip().split(':::')
		print(token, topic, tfidf_sum/num)
		prev = topic_token
		num = 1
		tfidf_sum = tfidf
	else:
		num += 1
		tfidf_sum += tfidf

if prev is not None and num > 0:
	token, topic = prev.strip().split(':::')
	print(token, topic, tfidf_sum/num)
