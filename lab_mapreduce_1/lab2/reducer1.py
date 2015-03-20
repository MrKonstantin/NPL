import sys

total = 0
for line in sys.stdin:
	total += int(float(line))

print(total)