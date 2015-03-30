import sys

for line in sys.stdin:
	url, count = line.strip().split('\t')
	t = - int(count)
	if sys.version_info.major == 2:
		t += sys.maxint
	else:
		t += sys.maxsize

	print(str(t) + '\t' + count + '\t' + url)
