#! usr/bin/env python3

import argparse

#Create an argument parser object ('parser') that will hold all the information
#necessary to parse the command line
parser = argparse.ArgumentParser(description = "generates a PBS commandline script for running this code")

#add positional arguments, i.e., the required input
parser.add_argument("dna_file", help = "path to the file that holds your DNA sequence")
parser.add_argument("info_file", help = "path to the file that holds your exon & intron information")

#Parse the command line arguments
args = parser.parse_args()

#Set paths to files to run
fsa_path = "/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/watermelon_files/"
gff_path = "/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/watermelon_files/"

#Designate dna & info files to run
fsa_file = fsa_path + args.dna_file
gff_file = gff_path + args.info_file


#USE BIOPYTHON TO PARSE THE FASTA FILE
from Bio import SeqIO
print("\nGENOME:")
for record in SeqIO.parse(fsa_file, "fasta"):
	print(record.id)
	print(repr(record.seq))
	print(len(record))

#Read in watermelon fsa & gff files
gff = open(gff_file, "r")
fsa2 = open(fsa_file).read()

#Write a function to calculate GC content
def get_GC_content(sequence, sigfigs = 2):
	g_content = sequence.count('G')
	c_content = sequence.count('C')
	gc_content = (g_content + c_content) / len(sequence)
	return round(gc_content, sigfigs)

#Parse files & extract all features of genome
print("\nGC CONTENT OF SEQUENCES:")
seqnumber = 1
for line in gff:
	line = line.rstrip("\n")
	#[sequence, source, feature, start, end, length, strand, phase, attributes] = line.split("\t")
	fields = line.split("\t")
	start = int(fields[3]) - 1
	stop = int(fields[4]) - 1
	output = fsa2[start:stop]
	name = fields[8]
	name_characters = name[0:10]
	print("Sequence", seqnumber, "a.k.a. " + name_characters + " ~", get_GC_content(output))
	seqnumber = seqnumber + 1
gff.close()
