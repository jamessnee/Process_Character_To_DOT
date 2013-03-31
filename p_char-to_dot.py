#! /usr/bin/env python 
import sys
import re

if __name__=="__main__":
	in_filename = sys.argv[1]
	out_filename = sys.argv[2]
	print "Reading from: "+in_filename
	print "Writing to: "+out_filename

	in_file = open(in_filename,'r')
	out_file = open(out_filename,'w')

	out_file.write("digraph test{\n")
	
	line = in_file.readline()
	while line:
		line = line[:line.rfind(',')]
		to_write = re.sub('[:,]',' -> ',line)
		out_file.write(to_write+';\n')
		line = in_file.readline()
	
	out_file.write("}")
	in_file.close()
	out_file.close()
