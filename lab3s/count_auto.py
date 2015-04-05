import sys

N = 0

for line in sys.stdin:
	try:
		url, a = line.strip().split('\t')
		if a == '1':
			N += 1
	except:
		continue

print(N)
