#! usr/bin/env python3

from __future__ import division

#To rename an existing file, we simply import the os module, then use the os.rename function
import os
#os.rename("old.txt", "new.txt") #This can also be done using filepaths if not working on Jupyter

#Use os.mkdir to create directories. Include the whole filepath to the new folder. If you are creating 
#a bunch of new folders within each other, you can also use os.mkdirs
    #os.mkdir("home/erichagen1/Desktop/newfolder")
    #os.mkdirs("home/erichagen1/Desktop/newfolder/garbage/bobdylanisgarbage/yeet")

#To copy something to a new place, use the shutil module
    #Use .copy for a file:
        #shutil.copy("home/erichagen1/Desktop/old.txt", "home/erichagen1/Downloads/old.txt")
    #Use .copytree for a folder:
        #shutil.copytee("home/erichagen1/Desktop/oldfolder", "home/erichagen1/Desktop/newfolder")
        
#You can even test whether a file exists:
    #if os.path.exists("home/erichagen/Desktop/old.txt"):
        #do (something)

#Removing files:
    #Remove a single file:
        #os.remove("home/erichagen/Desktop/old.txt")
    #Remove an empty folder:
        #os.rmdir("home/erichagen/Desktop/emptyfolder")
    #Remove a folder with stuff in it:
        #shutil.rmtree("home/erichagen/Desktop/folder_with_stuff")
        
#To list the contents of a folder (the period in parentheses gives the contents of the current working directory):
    #for file_name in os.listdir("."):
        #print("one file name is " + file_name)
#You can also get contents of a different folder:
    #for file_name in os.listdir("/home/erichagen1/Desktop"):
        #print("one file name is " + file_name)
        
#Running external programs using Python:
import subprocess
    #subprocess.call("/Applications/myprogram")
#If we want to supply command-line options to the external program then we just include them in the string like so:
    #subprocess.call("/Applications/myprogram", shell = True)
#We can even run an external program and save the output to a variable in Python:
    #The following is an example using the Linux date program:
        #current_month = subprocess.check_output("/bin/date +%B", shell=True)
        
#To take interactive input from other people using your code, use the "input" function:
    #accession = input("Enter the accession name")

#To use command line arguments in our Python scripts, we import the sys module. We can then access the command line 
#arguments by using the special list sys.argv:
import sys
    #print(sys.argv)
    
#To print working directory in python:
cwd = os.getcwd()
print(cwd)

import shutil, sys

#END-OF-CHAPTER EXERCISES

#Binning DNA sequences

#Write a program which creates nine new folders – one for sequences between 100
#and 199 bases long, one for sequences between 200 and 299 bases long, etc. Write
#out each DNA sequence in the input files to a separate file in the appropriate folder.

#Create folders
os.chdir("/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/Python_Stuff/exercise_9_folder")
numbers = range(1,9)
for number in numbers:
    os.mkdir("sequences_" + str(number) + "00s")

#Write a function to create multiples of 100
def hundredfy(number):
    hundred = number * 100
    return hundred

#Assign files to folders
number = 1
for file in os.listdir("."):
	if file.endswith(".dna"):
		dna = open(file)
		for line in dna:
			sequence = line.rstrip("\n")
			seq_length = len(sequence)
			range_numbers = range(1,9)
			for number in range_numbers:
				if seq_length >= hundredfy(number) and seq_length < hundredfy(number + 1):
					folder = "sequences_" + str(number) + "00s"
					path = folder + "/" + str(seq_length) + ".dna"
					file_content = open(path, "w")
					file_content.write(sequence)
					file_content.close()

#Check contents of folders:
range_numbers = range(1,9)
for number in range_numbers:
    folder = "sequences_" + str(number) + "00s"
    directory = "/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/Python_Stuff/exercise_9_folder/" + folder
    for file_name in os.listdir(directory):
        print(file_name)

#Kmer counting

#Write a program that will calculate the number of all kmers of a given length across
#all DNA sequences in the input files and display just the ones that occur more than
#a given number of times. Your program should take two command line arguments –
#the kmer length, and the cutoff number.

#Convert command line arguments to variables
kmer_length = int(sys.argv[1])
count_cutoff = int(sys.argv[2])

#Define the function to split dna into kmers:
def split_dna(dna, kmer_length):
	kmer_list = []
	dna_length = len(dna)
	for start in range(0, dna_length - (kmer_length - 1), 1):
		kmer = dna[start:start + kmer_length]
		kmer_list.append(kmer)
	return kmer_list

#Code for the task:
kmer_counts = {}
range_numbers = range(1,9)
for number in range_numbers:
	folder = "sequences_" + str(number) + "00s"
	path = "/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/Python_Stuff/exercise_9_folder/" + folder
	for file in os.listdir(" "):
		if file.endswith(".dna"):
			dna_file = open(file)
			for line in dna_file:
				dna = line.rstrip("\n")
				for kmer in split_dna(dna, kmer_length):
					current_count = kmer_counts.get(kmer, 0)
					new_count = current_count + 1
					kmer_counts[kmer] = new_count

#Print kmers whose counts are above the cutoff
for kmer, count in kmer_counts.items():
	if count > count_cutoff:
		print(kmer + " : " + str(count))
