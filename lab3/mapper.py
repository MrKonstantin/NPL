import sys
from urlparse import urlparse
import urllib
import re

for line in sys.stdin:
	strip = line.strip().split('\t')
	if len(strip) == 3 and strip[0] != '-':
		url = urlparse(urllib.unquote(strip[2]).strip()).netloc.strip()
		url = re.sub(r'^www\.', '', url)	
		if len(url) > 0:
			print(strip[0]+'\t'+url)
