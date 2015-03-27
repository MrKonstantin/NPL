from sys import stdin

# Выводим top 350 записей
n = 0
for line in stdin:
	n += 1
	if n <= 350:
		s, count, url = line.strip().split('\t')
		print(url + '\t' + str(count))
