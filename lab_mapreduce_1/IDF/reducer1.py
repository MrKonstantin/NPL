#!/usr/local/bin/python3
import sys

# Считаем полное количество документов
total_doc = 0
for line in sys.stdin:
	total_doc += int(float(line))

print(total_doc)
