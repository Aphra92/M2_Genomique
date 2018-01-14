#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import matplotlib.pyplot as plt
import shutil
import sys

os.chdir('/home/hadrien/Bureau/Genomique/pep')

seq_adn={}
for infile in os.listdir('/home/hadrien/Bureau/Genomique/pep'):
	if infile.endswith('.pep'):
		seq_adn[infile] = {}
		seq_adn[infile]["hist"] = []
		seq_adn[infile]["orf"] = []
		seqfile=open(infile,'r')
		lines = seqfile.readlines()
		for line in lines:
			line = line.rstrip()
			if re.match('^>',line):
				nom = line
				seq_adn[infile]["orf"].append(nom);
				seq_adn[infile][nom]=''
			else:
				seq_adn[infile][nom] = seq_adn[infile][nom] + line
		seqfile.close()

rewrite = {}
for i in seq_adn:	# Nom du fichier
	rewrite[i] = {}
	rewrite[i]["liste"] = []	# Liste de gene a ne pas re écrire
	for gene in seq_adn[i]:		# Gene
		if gene != 'hist' and gene != 'orf':
			if len(seq_adn[i][gene]) < 4000:
				seq_adn[i]["hist"].append(len(seq_adn[i][gene]))
			else:
				rewrite[i]["liste"].append(gene)

for infile in rewrite:
	if len(rewrite[infile]["liste"]) != 0:
		# Chnage le nom du fichier actuel
		os.rename(infile, infile+'.old')
		# Reécris le fichier sans les gènes trop grand
		fout = open(infile, "w")
		for i in seq_adn[infile]["orf"]:
			if i not in rewrite[infile]["liste"]:
				fout.write("{}\n".format(i))
				pospep=0
				line_size=60
				seq_prot = seq_adn[infile][i]
				while (pospep < len(seq_prot)):
					line_seq = seq_prot[pospep:(pospep+line_size)]
					fout.write("{}\n".format(line_seq))
					pospep += line_size
		fout.close()

for infile in os.listdir('/home/hadrien/Bureau/Genomique/pep'):
	if infile.endswith('.pep'):
		print infile	
		# Faire le fichier
		plt.hist(seq_adn[infile]["hist"])
		plt.title(infile)
		plt.xlabel("Taille")
		plt.ylabel("Frequency")
		#plt.show()
		plt.savefig(infile+'.jpeg')
		plt.clf()

if (os.path.exists("/home/hadrien/Bureau/Genomique/graph") == False):
	os.mkdir("/home/hadrien/Bureau/Genomique/graph");
for element in os.listdir("/home/hadrien/Bureau/Genomique/pep"):
	if element.endswith('.jpeg'):
		shutil.copy(element,'/home/hadrien/Bureau/Genomique/graph');
		os.remove(element);
