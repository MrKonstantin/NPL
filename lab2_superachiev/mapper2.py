import sys

# Return (sort_key, count, url)
for line in sys.stdin:
	url, count = line.strip().split('\t')
	# Reverse the number
	t = sys.maxint - int(count)
	print(str(t) + '\t' + count + '\t' + url)
