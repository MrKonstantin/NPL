from sys import stdin
from heapq import heappush, heappop

url = None
prev = None
count = 0
heap = []
N = 350

for line in stdin:
        url = line.strip().split('\t')[0]
        if prev is None:
                prev = url

        if prev != url:
                #print(prev + '\t' + str(count))
                heappush(heap, (count, prev))
                if len(heap) > N:
                        heappop(heap)

                count = 1
                prev = url
        else:
                count += 1

if prev == url:
        #print(prev + '\t' + str(count))
        heappush(heap, (count, prev))
        if len(heap) > N:
                heappop(heap)

while heap:
        c, u = heappop(heap)
        print(u + '\t' + str(c))
