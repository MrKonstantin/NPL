import sys
import copy

f = open('user_categories.dat')
lines = f.readlines()

urls = {}
n = 0
cat = []
for line in lines:
	strip = line.strip().split('\t')
	urls[strip[2]] = [0, n]
	urls[strip[3]] = [1, n]
	urls[strip[4]] = [2, n]
	cat.append([0, 0, 0])
	n += 1


def mk_result(uc):
	final_cats = [0] * n
	i = 0
	for ucat in uc:
		ucat.sort()
		if sum(ucat) > 2 and ucat[1] != 0:
			final_cats[i] = 1
		i += 1
	return '\t'.join(str(x) for x in final_cats)


ucats = copy.deepcopy(cat)
prev = None

for line in sys.stdin:
	uid, url = line.strip().split('\t')
	if prev is None:
		prev = uid

	if uid == prev:
		if url in urls.keys():
			val = urls[url]
			ucats[val[1]][val[0]] += 1
	else:
		print(prev + '\t' + mk_result(ucats))
		
		ucats = copy.deepcopy(cat)
		prev = uid

print(prev + '\t' + mk_result(ucats))
