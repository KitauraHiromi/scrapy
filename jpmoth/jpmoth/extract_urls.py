# -*- coding:utf-8 -*-
import re

with open("jpmoth.txt", "r") as f:
	urls = []
	pattern =r'([a-z])\1{3}|index|\d|UNIDENTIFIED|[A-Z]{2}|~|eratta|records|unknown|unidentified|[A-Z]+.html|/$|search|shelp|spsp|book'
	exclude1 = re.compile(r"http://www.jpmoth.org/")
	exclude2 = re.compile(r"[_]")
	exclude3 = re.compile(pattern)
	for line in f:
		if exclude1.match(line) and exclude2.search(line):
			#print "1"
			if not exclude3.search(line):
				#print "2"
				urls.append(line)
	#重複を消す. 順番が滅茶苦茶になるらしい.
	urls = list(set(urls))
	#ここでソート
	urls.sort()
	with open ("jpmoth_urls.txt", "w") as fout:
		for element in urls:
			fout.write(element)