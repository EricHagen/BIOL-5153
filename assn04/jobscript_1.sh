#!/bin/bash

#PBS -N BLAST_question1
#PBS -q qcondo_public
#PBS -j oe
#PBS -m abe
#PBS -M erhagen@uark.edu
#PBS -o BLAST.$PBS_JOBID
#PBS -l nodes=1:ppn=8
#PBS -l walltime=00:00:30:00

cd $PBS_O_WORKDIR

module load blast

./blastn -query nad4L.fasta | makeblastdb -dbtype nucl -out mt -title mt

