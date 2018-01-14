#!/usr/bin/env python

import sys
import re

infile = sys.argv[1]
sp_file = sys.argv[2]

list_sp= {}
spfile=open(sp_file,'r')
lines = spfile.readlines()
for line in lines:
	tmp = line.split()
	list_sp[tmp[1]] = tmp[0]
spfile.close()

genome=re.sub('.predict','',infile)
predfile=open(infile,'r')
lines = predfile.readlines()
for line in lines:
	if re.match('^>',line):
		sys.stdout.write("{}".format(line))
	else:
		tmp = line.split()
		sys.stdout.write("{}_{}\t{}\t{}\t{}\t{}\n".format(tmp[0],list_sp[genome],tmp[1],tmp[2],tmp[3],tmp[4]))
predfile.close()
