from sys import stdin

# Выводим все записи, отсортированные по количеству запросов
for line in stdin:
		s, count, url = line.strip().split('\t')
		print(url + '\t' + str(count))
