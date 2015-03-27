from sys import stdin

# Return (sort_key, count, url)
for line in stdin:
	url, count = line.strip().split('\t')
	# Reverse the number
	t = 999999999999 - int(count)
	print(str(t) + '\t' + count + '\t' + url)
