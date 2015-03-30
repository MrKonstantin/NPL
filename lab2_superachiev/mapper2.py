import sys

maxint = 0
if sys.version_info.major == 2:
	maxint = sys.maxint
else:
	maxint = sys.maxsize

for line in sys.stdin:
	url, count = line.strip().split('\t')
	t = maxint - int(count)
	print(str(t) + '\t' + count + '\t' + url)
