#!/usr/bin/env python
# coding: utf-8




#read files
fq1 = [i[:-1] for i in open('data/interim/SRR6994363_1.trimmomatic.fastq').readlines()]
fq2 = [i[:-1] for i in open('data/interim/SRR6994363_2.trimmomatic.fastq').readlines()]





#choose only srtings with sequense
seq1 = fq1[1::4]
ind1 = list(range(1,len(seq1)+1,4))
seq2 = fq2[1::4]
ind2 = list(range(1,len(seq2)+1,4))





#count gc content
GC_1 = [round((seq.count('G') + seq.count('C'))/(len(seq)) * 100) for seq in seq1]
    
GC_2 = [round((seq.count('G') + seq.count('C'))/(len(seq)) * 100) for seq in seq2]





#GC_content values fron ncbi sra
Mycoplasma_hyorhinis_gc = 25.9
Clostridioides_difficile_gc = 28.5
Cercopithecinae_gc = 41
Measles_morbillivirus_gc = 47.4
Influenza_A_virus_gc = 43





#sorting reads by gc content
Mycoplasma_hyorhinis_1 = []
Clostridioides_difficile_1 = []
Cercopithecinae_1 = []
Measles_morbillivirus_1 = []
Influenza_A_virus_1 = []
dark_matter_1 = []
for i,gc in zip(ind1,GC_1):
    part = fq1[i-1:i+3]
    if gc > 22 and gc <= 28:
        Mycoplasma_hyorhinis_1.append(part)
    if gc > 26 and gc <= 31:
        Clostridioides_difficile_1.append(part)
    if gc > 38 and gc <= 43:
        Cercopithecinae_1.append(part)
    if gc >= 44 and gc <= 48:
        Measles_morbillivirus_1.append(part)
    if gc > 41 and gc <= 45:
        Influenza_A_virus_1.append(part)
    else:
        dark_matter_1.append(part)





Mycoplasma_hyorhinis_2 = []
Clostridioides_difficile_2 = []
Cercopithecinae_2 = []
Measles_morbillivirus_2 = []
Influenza_A_virus_2 = []
dark_matter_2 = []
for i,gc in zip(ind2,GC_2):
    part = fq2[i-1:i+3]
    if gc > 22 and gc <= 28:
        Mycoplasma_hyorhinis_2.append(part)
    if gc > 26 and gc <= 31:
        Clostridioides_difficile_2.append(part)
    if gc > 38 and gc <= 43:
        Cercopithecinae_2.append(part)
    if gc >= 44 and gc <= 48:
        Measles_morbillivirus_2.append(part)
    if gc > 41 and gc <= 45:
        Influenza_A_virus_2.append(part)
    else:
        dark_matter_2.append(part)





#saving results
with open('data/processed/SRR6994363_1.Mycoplasma_hyorhinis.trimmomatic.fastq', 'w') as f:
    for l in Mycoplasma_hyorhinis_1:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_1.Clostridioides_difficile.trimmomatic.fastq', 'w') as f:
    for l in Clostridioides_difficile_1:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_1.Cercopithecinae.trimmomatic.fastq', 'w') as f:
    for l in Cercopithecinae_1:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_1.Measles_morbillivirus.trimmomatic.fastq', 'w') as f:
    for l in Measles_morbillivirus_1:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_1.Influenza_A_virus.trimmomatic.fastq', 'w') as f:
    for l in Influenza_A_virus_1:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_1.dark_matter.trimmomatic.fastq', 'w') as f:
    for l in dark_matter_1:
        for k in l:
            f.write(k + '\n')


# save _2 files


with open('data/processed/SRR6994363_2.Mycoplasma_hyorhinis.trimmomatic.fastq', 'w') as f:
    for l in Mycoplasma_hyorhinis_2:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_2.Clostridioides_difficile.trimmomatic.fastq', 'w') as f:
    for l in Clostridioides_difficile_2:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_2.Cercopithecinae.trimmomatic.fastq', 'w') as f:
    for l in Cercopithecinae_2:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_2.Measles_morbillivirus.trimmomatic.fastq', 'w') as f:
    for l in Measles_morbillivirus_2:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_2.Influenza_A_virus.trimmomatic.fastq', 'w') as f:
    for l in Influenza_A_virus_2:
        for k in l:
            f.write(k + '\n')
            
with open('data/processed/SRR6994363_2.dark_matter.trimmomatic.fastq', 'w') as f:
    for l in dark_matter_2:
        for k in l:
            f.write(k + '\n')

