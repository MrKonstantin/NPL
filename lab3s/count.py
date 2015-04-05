import sys
import heapq

auto = 0
f = open('auto_number.txt')
for line in f.readlines():
	auto += int(line.strip()) 

heap = []

N = 100

def key(line):
	return line[0]

for line in sys.stdin:
	url, c = line.strip().split('\t')
	c = float(c)/auto
	heapq.heappush(heap, (c, url))

l = heapq.nlargest(N, heap, key = key)	
for (c, url) in l: 
	print '%s\t%.10f' % (url, c)
