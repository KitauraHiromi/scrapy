#!usr/bin/env python

import re
import glob
import os
__DEBUG__ = True

def get_hierarchy(filename):
	hierarchy = []
	with open(filename) as f:
		f.readline()			#skip first line
		line = f.readline()		#get second line
		tmp = re.findall(r"\([a-zA-Z+]*?\)", line)
		for i in range(len(tmp)):
			hierarchy.append(re.findall(r"[a-zA-Z+]+", tmp[i])[0])
		if(__DEBUG__):
			print line
			print hierarchy
		return hierarchy

def get_figure_url(filename):
	with open(filename, "r") as f:
		figure_url_list = []
		for line in f:
			try:
				figure_url_list.append(line.split('"')[3])
			except(IndexError):
				pass
		return figure_url_list


if __name__ == "__main__":
	with open("list.txt", "w") as f:
		filename_list = [os.path.basename(r) for r in glob.glob("html/*")]
		#print filename_list[0]
		for name in filename_list:
			tmp = name.split("%")
			hierarchy =  "http://www.jpmoth.org/"
			for element in tmp[0:-2]:
				hierarchy += element + "/"
			for url in get_figure_url("html/"+name):
				f.write(hierarchy + url + "\n")
