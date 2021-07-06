#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
author: Sitao Zhu
date: 2021/3/23 下午3:11
filename: pipeline_pysam.py
'''


import pysam
#pysam is a module for read and write SAM,BAM,VCF,BCF,BED,GFF,GTF,FASTA,FASTQ
print(pysam.__version__)

samfile = pysam.AlignmentFile('../../project/05.RPFdb/GSE43703/scripts_yang/D_RF_1/D_RF_1Aligned.sortedByCoord.out.bam','rb')
# for read in samfile.fetch('1',100,2000):
#     print(read)
# samfile.close()

pairedreads = pysam.AlignmentFile('allpaired.bam','wb',template=samfile)
# fetch 获取特定区段
for read in samfile.fetch(reference='1',start=100,end=20000):
    if not read.is_paired:
        pairedreads.write(read)

pairedreads.close()
# samfile.close()


# 循环每一个位点，输出每一个位点的覆盖的read，以及对应的碱基
for pileupcolumn in samfile.pileup(reference='1',start=100,end=2000):
    print('\ncoverage at base %s = %s'%(pileupcolumn.pos,pileupcolumn.n))
    for pileupread in pileupcolumn.pileups:
        if not pileupread.is_del and not pileupread.is_refskip:
            print('\tbase in read %s = %s'%(pileupread.alignment.query_name,pileupread.alignment.query_sequence[pileupread.query_position]))

print(samfile.count(reference='1',start=100,end=20000))
print(samfile.count_coverage(reference='1',start=100,end=200))
pysam.IndexedReads(samfile).find('SRR652152.1.50609578')

samfile.close()

