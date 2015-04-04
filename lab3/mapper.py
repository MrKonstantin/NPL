import sys
from urlparse import urlparse
import urllib
import re

for line in sys.stdin:
	split = line.strip().split('\t')
	if len(split) == 3 and split[0] != '-':
		url = urlparse(urllib.unquote(split[2]).strip()).netloc.strip()
		url = re.sub(r'^www\.', '', url)	
		if len(url) > 0:
			uid = split[0]
			print '%s\t%s' % (uid, url)
