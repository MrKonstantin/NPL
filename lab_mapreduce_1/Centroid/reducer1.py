from sys import stdin

prev = None
num = 0
tfidf_sum = 0

for line in stdin:
	topic_token, tfidf = line.strip().split('\t')

	if prev is None:
		prev = topic_token
		num = 1
		tfidf_sum = tfidf
	elif prev[0] != topic_token:
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