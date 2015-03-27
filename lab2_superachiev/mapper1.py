# Для каждой строки выдаем url
from sys import stdin

for line in stdin:
	split = line.strip().split('\t')
	if len(split) == 3:
		url = split[2]
		print(url)
