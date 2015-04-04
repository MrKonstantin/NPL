import sys

f = open('user_categories.dat')
lines = f.readlines()


urls = {}
n = 0
ucats = []

for line in lines:
	strip = line.strip().split('\t')
	urls[strip[2]] = (0, n) ### (url number, feature number) 
	urls[strip[3]] = (1, n)
	urls[strip[4]] = (2, n)
	ucats.append([0,0,0])
	n += 1

prev = None
uid = None

for line in sys.stdin:
	uid, url = line.strip().split('\t')

	if prev is None:
		prev = uid

	if uid == prev:
		if url in urls.keys():
			un, fn = urls[url]
			ucats[fn][un] += 1
	else:
		final_cats = []
		for ucat in ucats:
			ucat.sort()
			if sum(ucat) > 2 and ucat[1] != 0:
				final_cats.append("1")
			else:
				final_cats.append("0")

		f = '\t'.join(final_cats)
		print '%s\t%s' % (prev, f)

		prev = uid
		ucats = []
		for x in range(0, n):
			ucats.append([0,0,0])

		if url in urls.keys():
			un, fn = urls[url]
			ucats[fn][un] += 1

if prev == uid:
	final_cats = []
	for ucat in ucats:
		ucat.sort()
		if sum(ucat) > 2 and ucat[1] != 0:
			final_cats.append("1")
		else:
			final_cats.append("0")

	f = '\t'.join(final_cats)
	print '%s\t%s' % (prev, f)
