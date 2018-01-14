#!/usr/bin/env python

import sys
import os
import glob
import re

if (len(sys.argv) != 2):
    sys.exit(sys.stdout.write("\n\tUsage : {} <directory>\n\n".format(sys.argv[0])))
    
if (os.path.exists(sys.argv[1]) == False) or (os.path.isdir(sys.argv[1]) == False):
    sys.exit(sys.stdout.write("\n\tDirectory '{}' does not exist !\n\n".format(sys.argv[1])))

rep = sys.argv[1]
os.chdir(rep)

nb_files = 0
for file_name in sorted(glob.glob('*.fa')):
    nb_files += 1
    genome_name=re.sub('.fa','',file_name)
    
    infile=open(file_name,'r')
    lines = infile.readlines()

    nb_chrom = 0
    genome_size = 0
    composition = {}
    for line in lines:
        if re.match('^>',line):
            nb_chrom += 1
        else:
            line = line.rstrip()
            genome_size += len(line)
            for nuc in line:
                if composition.has_key(nuc):
                    composition[nuc] = composition[nuc]+1
                else:
                    composition[nuc] = 1
                
    infile.close()
    
    nb_ACGT = composition['A']+composition['C']+composition['G']+composition['T']
    gc_percent = ((composition['G']+composition['C'])/float(nb_ACGT))*100

    sys.stdout.write("\n{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(nb_files,genome_name,nb_chrom,genome_size,nb_ACGT,(genome_size-nb_ACGT),gc_percent))

    for nuc in sorted(composition.keys()):
        sys.stdout.write("\t{} [{}]".format(nuc,composition[nuc]))
    
sys.stdout.write("\n\n")
    