import sys
import urllib
from urlparse import urlparse
import re

f = open('autousers_lab3s.txt')

auto = []
for line in f.readlines():
	auto.append(line.strip())

for line in sys.stdin:
	split = line.strip().split('\t')
	if len(split) == 3:
		uid, ts, url = split
		url = urlparse(urllib.unquote(url).strip()).netloc.strip()
		url = re.sub(r'^www\.', '', url)
	elif len(split) == 2:
		uid, ts = split
		url = ""
	else:
		continue
		
	is_auto = 0
	if uid in auto:
		is_auto = 1

	print '%s\t%s' % (url, is_auto)
