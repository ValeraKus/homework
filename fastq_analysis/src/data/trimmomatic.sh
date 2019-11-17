#!/bin/bash

java -jar ~/Trimmomatic-0.39/trimmomatic-0.39.jar SE -phred33 data/raw/SRR6994363_1.fastq data/interim/SRR6994363_1.trimmomatic.fastq LEADING:28 TRAILING:28 SLIDINGWINDOW:5:28 MINLEN:30
java -jar ~/Trimmomatic-0.39/trimmomatic-0.39.jar SE -phred33 data/raw/SRR6994363_2.fastq data/interim/SRR6994363_2.trimmomatic.fastq LEADING:28 TRAILING:28 SLIDINGWINDOW:5:28 MINLEN:30

fastqc -o reports/ data/interim/SRR6994363_2.trimmomatic.fastq 
fastqc -o reports/ data/interim/SRR6994363_1.trimmomatic.fastq 
