#! usr/bin/env python3

import argparse
import csv

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

#Open gff file
with open(gff_file, 'r') as gff:

	#Create a csv reader object to open the gff file
	csvreader = csv.reader(gff, delimiter = "\t")

	#Import the SeqIO module & open the fsa file with it
	from Bio import SeqIO
	fsa = SeqIO.read(fsa_file, 'fasta')

	#Print the fasta file
	print("\nGENOME:")
	print(fsa)

	#Write a function to calculate GC content
	def get_GC_content(sequence, sigfigs = 2):
		g_content = sequence.count('G')
		c_content = sequence.count('C')
		gc_content = (g_content + c_content) / len(sequence)
		return round(gc_content, sigfigs)

	#Get GC content values
	print("\nGC CONTENT OF SEQUENCES:")
	seqnumber = 1
	fullsequence = fsa.seq
	for row in csvreader:
		start = int(row[3]) - 1
		stop = int(row[4]) - 1
		output = fullsequence[start:stop]
		name = row[8]
		name_characters = name[0:10]
		print("Sequence", seqnumber, "a.k.a. " + name_characters + " ~", get_GC_content(output))
		seqnumber = seqnumber + 1

#Close the gff file
gff.close()
