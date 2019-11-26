#! usr/bin/env python3

import argparse
import csv
from Bio import SeqIO
from collections import defaultdict

#Set paths to files to run
fsa_path = "/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/watermelon_files/"
gff_path = "/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/watermelon_files/"

#Write a function to designate arguments
def get_args():
	#Create an argument parser object ('parser') that will hold all the information
	#necessary to parse the command line
	parser = argparse.ArgumentParser(description = "generates a PBS commandline script for running this code")
	#add positional arguments, i.e., the required input
	parser.add_argument("dna_file", help = "path to the file that holds your DNA sequence")
	parser.add_argument("info_file", help = "path to the file that holds your exon & intron information")
	#Parse the command line arguments
	return parser.parse_args()

#Write a function to read the GFF file
def read_gff(gff_file):
	gff = open(gff_file, "r")
	return gff

#Write a function to parse the GFF file
def parse_the_gff(gff):
	csvreader = csv.reader(gff, delimiter = "\t")
	return csvreader

#Write a function to read the fsa file
def read_fsa(fsa_file):
	#Use SeqIO to open the fsa file
	fsa = SeqIO.read(fsa_file, 'fasta')
	#Print the fasta file
	print("\nGENOME:")
	print(fsa) #Use fsa.seq to print the entire sequence
	return fsa.seq

#Write a function to calculate GC content
def get_GC_content(sequence, sigfigs = 2):
	g_content = sequence.count('G')
	c_content = sequence.count('C')
	gc_content = (g_content + c_content) / len(sequence)
	return round(gc_content, sigfigs)

#Write a function to get the reverse complement of a sequence
def reverse__complement(sequence):
	reverse = sequence.reverse_complement()
	return reverse

#Get GC content values
def print_GC_content(fsa, csvreader):
	print("\nGC CONTENT OF SEQUENCES:")
	seqnumber = 1
	for row in csvreader:
		start = int(row[3]) - 1
		stop = int(row[4]) - 1
		output = fsa[start:stop]
		name = row[8]
		name_characters = name[0:10]
		print("Sequence", seqnumber, "a.k.a. " + name_characters + " ~ " + "GC content of: ", get_GC_content(output))
		if row[6] == "-":
			start = int(row[3]) - 1
			stop = int(row[4]) - 1
			output = fsa[start:stop]
			c = reverse__complement(output)
			print("This is a minus strand, and its reverse complement is:")
			print(c)
			print("\n")
		else:
			print("This is a + strand\n")
		seqnumber = seqnumber + 1

#Write the main function through which the whole program will be executed
def main():
	gff = read_gff(gff_file)
	csvreader = parse_the_gff(gff)
	fsa = read_fsa(fsa_file)
	print_GC_content(fsa, csvreader)

#Call the function we defined above
args = get_args()

#Designate dna & info files to run
fsa_file = fsa_path + args.dna_file
gff_file = gff_path + args.info_file

#Execute the program by calling the main function
if __name__ == "__main__":
	main()








#4-29 class stuff

#Dictionary to hold CDS sequences, key = gene name, value = dictionary #2 where key = exon number, value = the sequence
coding_seqs = defaultdict(dict)

if not line:
	continue
else:
	begin = int(line[3]) - 1
	end = int(line[4])
	strand = line[6]
	feature = line[2]
	attribute = line[8]
	species = line[0]
feature_sequence = genome[begin:end]
gene_name = exon_info[0].split()[1]
exon_number = exon_info[0].split()[]
exon_info = attributes.split(" ; ")
if len(exon_info[0].split()) > 2:
	exon_number = exon_info[0].split()[-1]
	if gene_name in coding_seqs:
		#store the coding seq for this exon
	else:
		#first time encountering this gene, so declare the dictionary for it
		coding_seqs[gene_name] = {}
		#store the coding seq for this exon
		coding_seqs[gene_name][exon_number] = feature_sequence 
else:
	print('>' + line[0].replace(' ', '_') + '_' + gene_name)
	print(feature_sequence)

#done reading the GFF file, loop over coding_seqs to print the CDS sequence
#gene = gene name, exons = dictionary of exon seqs, key = exon_num, value = exon_seq
for gene, exons in coding_seqs.items():
	#make a variable to hold the concatenated CDS sequence
	cds_for_this_gene = ''
	#loop over all the exons for this particular gene. IMPORTANT: need to sort the exons first
	#print the fasta header for this gene
	print('>', line[0].replace(' ', '_') + '_' + gene)
	for exon_num, exon_seq in sorted(exons.items()):
		#print(gene, exon_num, exon_seq)
		cds_for_this_gene += exon_seq
	#print the CDS sequence for this gene
	print(cds_for_this_gene)

