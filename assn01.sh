#!
/bin/bash/

#assn01-1
cd ~
find . -type f | grep "nad"

#assn01-2
#I used top. This command takes up around 6% of my CPU.
#MemRegions: 271474 total, 2810M resident, 50M private, 449M shared. PhysMem: 7899M used (3706M wired), 292M unused.

#assn01-3
cd /Users/erichagen1/Desktop/University\ of\ Arkansas\ Stuff/Fall\ 2019\ Semester/Practical\ Programming/watermelon_files
grep "misc_feature" watermelon.gff | sort -k7gr > IR_regions.gff

#assn01-4
grep -v "misc_feature" watermelon.gff | sort -k7gr > non_IR_regions.gff
wc -l IR_regions.gff
wc -l non_IR_regions.gff
#There are actually 107 sequences from outside the inverted repeat region, which is greater than the 37 sequences from the region. So more chloroplast fragments come from 
#outside the IR.

#assn01-5
#EcoRI - GAATTC
#BamHI - GGATCC
cd watermelon_nt
grep "GGATCC" *.fasta | grep -v "GAATTC" > assn01-5.fa
head assn01.5.fa
wc -l assn01-5.fa
#There are 5 genes with a BamHI site and no EcoRI site.

#assn01-6
cd example_files
head -n 1000 shaver_etal.csv | tail -n 500 > assn01-6.csv

#assn01-7
column -t fruit.txt | sort -k2r | sort -k3

