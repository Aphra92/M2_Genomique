#!/usr/bin/env python
# -*- coding: utf-8 -*-

# usage : ./auto_glimmer.py EMBL_dna Res_glimmer

import sys
import os
import glob
import re
import shutil

if (os.path.exists("/home/hadrien/Bureau/Genomique/results") == False):
	os.mkdir("/home/hadrien/Bureau/Genomique/results");
if (os.path.exists("/home/hadrien/Bureau/Genomique/annexe") == False):
	os.mkdir("/home/hadrien/Bureau/Genomique/annexe");
if (os.path.exists("/home/hadrien/Bureau/Genomique/pep") == False):
	os.mkdir("/home/hadrien/Bureau/Genomique/pep");

genomes_dir = "/home/hadrien/Bureau/Genomique/Sequences"
result_dir = "/home/hadrien/Bureau/Genomique/glimmer3.02/results"
glimmer_scripts ="/home/hadrien/Bureau/Genomique/glimmer3.02/scripts"

os.chdir(genomes_dir)

nb_files = 0
for file_name in sorted(glob.glob('*.fa')):
    nb_files += 1
    genome_name=re.sub('.fa','',file_name)
    sys.stdout.write("\n[***\t{}\t{}\t***]\n\n".format(nb_files,genome_name))
    os.system(glimmer_scripts + "/g3-from-scratch.csh " + file_name + " " + genome_name)
    os.system("../rename_pred.py " + genome_name + ".predict ../Species_list.txt > " + genome_name +".predict_renamed")
    os.system("../extract.py " + genome_name + ".fa " + genome_name + ".predict_renamed > " + genome_name + ".cds")
    os.system("../translate.py " +  genome_name + ".cds ../code_genetique.txt > " + genome_name +".pep");

# Suppression des fichiers en trop et deplacement dans le dossier resultat	
for element in os.listdir("/home/hadrien/Bureau/Genomique/Sequences"):
	if element.endswith('.detail'):
		shutil.copy(element,'/home/hadrien/Bureau/Genomique/annexe');
		os.remove(element);	
	if element.endswith('.train'):
		shutil.copy(element,'/home/hadrien/Bureau/Genomique/annexe');
		os.remove(element);		
	if element.endswith('.icm'):
		shutil.copy(element,'/home/hadrien/Bureau/Genomique/annexe');
		os.remove(element);	
	if element.endswith('.longorfs'):
		shutil.copy(element,'/home/hadrien/Bureau/Genomique/annexe');
		os.remove(element);	
	if element.endswith('.predict'):
		shutil.copy(element,'/home/hadrien/Bureau/Genomique/results');
		os.remove(element);	
	if element.endswith('.predict_renamed'):
		shutil.copy(element,'/home/hadrien/Bureau/Genomique/annexe');
		os.remove(element);	
	if element.endswith('.cds'):
		shutil.copy(element,'/home/hadrien/Bureau/Genomique/annexe');
		os.remove(element);	
	if element.endswith('.pep'):
		shutil.copy(element,'/home/hadrien/Bureau/Genomique/pep');
		os.remove(element);
