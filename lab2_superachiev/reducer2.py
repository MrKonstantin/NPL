from sys import stdin

for line in stdin:
		s, count, url = line.strip().split('\t')
		print(url + '\t' + str(count))
