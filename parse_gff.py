#! usr/bin/env python3

#Read in watermelon fsa & gff
with open("/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/watermelon_files/watermelon.fsa") as open_fsa:
    fsa = open_fsa.read().splitlines()
gff = open("/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/watermelon_files/watermelon.gff", "r")

#Print just the fsa genome
print("\nWATERMELON FSA GENOME:\n")
lines = fsa[1:]
print(lines)

#Reopen the fsa file for use in the second part:
fsa2 = open("/Users/erichagen1/Desktop/University_of_Arkansas_Stuff/Spring_2019_Semester/Practical_Programming/watermelon_files/watermelon.fsa").read()

#Write a function to calculate GC content
def get_GC_content(sequence, sigfigs = 2):
	g_content = sequence.count('G')
	c_content = sequence.count('C')
	gc_content = (g_content + c_content) / len(sequence)
	return round(gc_content, sigfigs)

#Parse files & extract all features of genome
startsandstops = []
print("\nGC CONTENT OF SEQUENCES:")
seqnumber = 1
for line in gff:
	line = line.rstrip("\n")
	#[sequence, source, feature, start, end, length, strand, phase, attributes] = line.split("\t")
	fields = line.split("\t")
	start = int(fields[3])
	stop = int(fields[4])
	output = fsa2[start:stop]
	startsandstops.append(output)
	print("Sequence", seqnumber, "~", get_GC_content(output))
	seqnumber = seqnumber + 1
gff.close()
