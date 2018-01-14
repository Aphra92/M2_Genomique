#!/usr/bin/env python

# usage :

import sys
import re

infile = sys.argv[1]
genetic_code_file = sys.argv[2]

code_genetique={}
code=open(genetic_code_file,'r')
lines = code.readlines()
for line in lines:
	line = line.rstrip()
	tmp = line.split()
	code_genetique[tmp[0]]=tmp[2]
code.close()

liste=[]
seq_adn={}
seqfile=open(infile,'r')
lines = seqfile.readlines()
for line in lines:
	line = line.rstrip()
	if re.match('^>',line):
		nom=line
		liste.append(nom)
		seq_adn[nom]=''
	else:
		seq_adn[nom]= seq_adn[nom] + line
seqfile.close()

for i in liste:
	sys.stdout.write("{}\n".format(i))
	pos=0
	seq_prot=''
	tmp_seq=seq_adn[i]
	while (pos < len(tmp_seq)):
		codon=tmp_seq[pos:(pos+3)]
		if code_genetique.has_key(codon):
			seq_prot=seq_prot + code_genetique[codon]
		else:
			seq_prot=seq_prot + "X"
		pos += 3
	pospep=0
	line_size=60
	while (pospep < len(seq_prot)):
		line_seq = seq_prot[pospep:(pospep+line_size)]
		sys.stdout.write("{}\n".format(line_seq))
		pospep += line_size
