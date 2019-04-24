#! /bin/bash

#assn02-1
echo TR-{808..8008}

#assn02-2
echo '#! /bin/bash'
cd /tmp/copies
for file in *.fasta; do echo my_python_script.py $file '>' ${file%.fasta}.out; done

#assn02-3
nano /.bash_profile
alias   list='clear; ls -l'

#assn02-4
cd /Users/erichagen1/Desktop/University\ of\ Arkansas\ Stuff/Fall\ 2019\ Semester/Practical\ Programming/assn02/gene_trees 
find . -name "*.fasta" | wc -l
#15085 files

#assn02-5
find . -name "*.tre" | wc -l
#14640 trees

#assn02-6
find . -name "*.sched" | wc -l
#15262 analyses

#assn02-7
for i in *.fasta; do test -e ${i%.fasta}_raxml.tre && echo $i "yes" >> names.txt || echo $i "no" >> names.txt; done
grep "no" names.txt | wc -l
#445 .fasta files have no corresponding .tre file, which is the same answer you get from subtracting 15085 - 14640 >.<

#assn02-8
for i in *.sched; do if grep -q "Program Return Code: 0" $i; then echo $i "successful" >> analysis.txt; else echo $i "unsuccessful" >> analysis.txt; fi; done
grep "unsuccessful" analysis.txt | wc -l 
#Of the 15262 .sched files, 45 were unsuccessful.

#assn02-9
for i in *.fasta; do test -e ${i%.fasta}_raxml.tre && echo $i  "yes" >> garbage.txt || echo write_raxml_job_script.py $i '>' ${i%.fasta}.pbs >> cluster_computing.txt; done
wc -l cluster_computing.txt
rm garbage.txt
