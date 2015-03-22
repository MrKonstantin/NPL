
import sys
import happybase

connection = happybase.Connection('127.0.0.1')
table = connection.table('konstantin.kiselev')

for line in sys.stdin:
	try:
		uid, tmstp, url = line.strip().split('\t')
		uid = int(float(uid))
		tmstp = int(float(tmstp)*1000)
		print(uid, tmstp, url)
		#if uid % 256 == 240:
			#table.put(str(uid), {'data:url': url}, timestamp=tmstp)
	except:
		continue
