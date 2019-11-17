#!/bin/bash

#download paired reads
fastq-dump --outdir data/raw --origfmt --split-3 -I SRR6994363

#initial report
fastqc -o reports/ data/raw/SRR6994363_*.fastq

#trimm reads by quality with trimmomatic
java -jar ~/Trimmomatic-0.39/trimmomatic-0.39.jar SE -phred33 data/raw/SRR6994363_1.fastq data/interim/SRR6994363_1.trimmomatic.fastq LEADING:28 TRAILING:28 SLIDINGWINDOW:5:28 MINLEN:30
java -jar ~/Trimmomatic-0.39/trimmomatic-0.39.jar SE -phred33 data/raw/SRR6994363_2.fastq data/interim/SRR6994363_2.trimmomatic.fastq LEADING:28 TRAILING:28 SLIDINGWINDOW:5:28 MINLEN:30

#interim reports
fastqc -o reports/ data/interim/SRR6994363_2.trimmomatic.fastq
fastqc -o reports/ data/interim/SRR6994363_1.trimmomatic.fastq


#sorting by GC content from ncbi rsa
python3 src/data/sort.by.gc.content.py

#final report
fastqc -o reports/final data/processed/SRR6994363*
