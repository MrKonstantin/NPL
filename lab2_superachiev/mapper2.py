import sys

for line in sys.stdin:
	url, count = line.strip().split('\t')
	t = sys.maxint - int(count)
	print(str(t) + '\t' + count + '\t' + url)
