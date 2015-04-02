import sys

f = open('user_categories.dat')
lines = f.readlines()


urls = {}
n = 0
ucats = []

try:
	for line in lines:
		strip = line.strip().split('\t')
		urls[strip[2]] = [0, n]
		urls[strip[3]] = [1, n]
		urls[strip[4]] = [2, n]
		ucats.append([0,0,0])
		n += 1
except Exception as e:
	print(e)

prev = None

for line in sys.stdin:
	try:
		uid, url = line.strip().split('\t')

		if prev is None:
			prev = uid

		if uid == prev:
			if url in urls.keys():
				val = urls[url]
				ucats[val[1]][val[0]] += 1
		else:
			final_cats = []
			for ucat in ucats:
				ucat.sort()
				if sum(ucat) > 2 and ucat[1] != 0:
					final_cats.append("1")
				else:
					final_cats.append("0")
		
			print(prev + '\t' + '\t'.join(final_cats))

			prev = uid
			ucats = []
			for x in range(0, n):
				ucats.append([0,0,0])

			if url in urls.keys():
				val = urls[url]
				ucats[val[1]][val[0]] += 1
	except Exception as e:
		print(e)

try:
	final_cats = []
	for ucat in ucats:
		ucat.sort()
		if sum(ucat) > 2 and ucat[1] != 0:
			final_cats.append("1")
		else:
			final_cats.append("0")

	print(prev + "\t" + "\t".join(final_cats))

except Exception as e:
	print("Error: " + e)
