from sys import stdin

for line in stdin:
	try:
		split = line.strip().split('\t')
	except:
		continue

	if len(split) == 3 and split[0] != '-':
		url = split[2]
		print(url + '\t' + '1')
