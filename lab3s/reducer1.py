import sys

auto_urls = ['avto-russia.ru', 'bmwclub.ru', 'cars.ru']

fr = [0, 0] ### [auto url number, url number]
prev = None

for line in sys.stdin:
	try:
		url, is_auto = line.strip().split('\t')
		is_auto = int(is_auto)
	except:
		continue

	if prev is None:
		prev = url

	if prev == url:
		if is_auto == 1:
			fr[0] += 1
		fr[1] += 1
	else:
		c = float(0)
		if fr[0] > 0 and fr[1] > 0:
			try:
				c = float(fr[0]**2)/fr[1]
			except:
				pass

		print '%s\t%s' % (prev, c)

		fr = [0, 0]
		if is_auto == 1:
			fr[0] += 1
		fr[1] += 1
		prev = url

c = float(0)
if fr[0] > 0 and fr[1] > 0:
	try:
		c = float(fr[0]**2)/fr[1]
	except:
		pass

print '%s\t%s' % (prev, c)
