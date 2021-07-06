#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: viral_utr_retrieve.py
date: 2021/6/15 上午11:30
author: Sitao Zhu
mail: zhusitao1990@163.com
'''

import os
import re
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import GenBank
import argparse
'''
程序设计来进行病毒的utr抓取，用来合成utr文库
'''

def parse_args():
    parser = argparse.ArgumentParser(description="virus 5'UTR and 3'UTR retrieve")
    parser.add_argument('--legth5', '-f', type=int, help='utr5 length cutoff')
    parser.add_argument('--length3', '-r', type=int, help='utr3 length cutoff')
    parser.add_argument('--genbank', '-g', type=str, help='genbank path')
    parser.add_argument('--taxonomy', '-t', type=str, help='taxonomy path')
    return parser.parse_args()

def extract_taxonomy(taxonomy_path):
    accession = dict()
    with open(taxonomy_path,'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('##'):
                continue
            array = line.split('\t')
            acc, neig = array[0],array[2]
            if neig not in accession:
                accession[neig] = [acc]
            else:
                accession[neig].append(acc)
    # human,vertebrates; land plants
    acc_list = []
    for item in ['human,vertebrates', 'land plants']:
        for acc in accession[item]:
            acc_list.append(acc)
    return acc_list

def feature_location_parse(x):
    p = re.compile(r'(\d+)\.\.(\d+)')
    match = p.search(x)
    if match:
        s = match.group(1)
        e = match.group(2)
        return int(s),int(e)
    else:
        return 0,0

def read_genebank(genebank_path, acc_list):
    '''
    读取GeneBank的注释文件
    :param genebank_path: gene bank path
    :return:
    '''
    with open(genebank_path) as handle:
        for record in GenBank.parse(handle):
            # print(type(record))
            if record.locus not in acc_list:
                continue
            if record.locus == 'NC_028139':
                continue
            # print(record.locus)
            # print(record.size)
            # print(record.residue_type)
            # print(record.version)
            # print(record.pid)
            # print(record.accession)
            # print(record.segment)
            # print(record.organism)
            # print(record.taxonomy)
            # print(record.references)
            # print(record.features)
            # print('origin,',record.origin)
            # print(len(record.sequence))
            feature_count = 0
            for feature in record.features:

                start, end = feature_location_parse(feature.location)
                # print(start, end)
                seq = record.sequence[start - 1:end]
                seq = Seq(seq)

                if feature.key == 'gene':
                    feature_count += 1
                    if 'complement' not in feature.location:
                        # 正义链
                        # pep = seq.translate()
                        print(record.locus, "+", feature.key, seq)
                    else:
                        # 反义链
                        seq = seq.reverse_complement()
                        # pep = seq.translate()
                        print(record.locus, '-', feature.key, seq)
            # print('feature count:', feature_count)



def parse_genebank(genebank_path, acc_list, utr5_len, utr3_len):

    for record in SeqIO.parse(genebank_path,'genbank'):
        # print(len(record.seq))
        if record.name not in acc_list:
            continue
        for feature in record.features:
            if feature.type == "CDS":
                nstart = feature.location.start
                nend = feature.location.end
                strand = feature.strand
                cds_seq = feature.location.extract(record.seq) # 提取序列
                # seq = record.seq[nstart:nend] # 采用索引对多个区间不使适用

                if strand == 1:
                    if nstart >= utr5_len:
                        utr5 = record.seq[nstart - utr5_len:nstart]
                    else:
                        utr5 = record.seq[:nstart]
                    # utr3 取整个fragment上的最后的定长的碱基
                    if len(record.seq) - nend >= utr3_len:
                        utr3 = record.seq[nend:nend+utr3_len]
                    else:
                        utr3 = record.seq[nend:]

                    print(record.id, feature.type, nstart, nend, strand, 'utr5', len(utr5), utr5)
                    print(record.id, feature.type, nstart, nend, strand, 'utr3', len(utr3), utr3)
                elif strand == -1:
                    if len(record.seq) - nend >= utr5_len:
                        utr5 = record.seq[nend:nend+utr5_len]
                    else:
                        utr5 = record.seq[nend:]
                    if nstart - utr3_len >= 0:
                        utr3 = record.seq[nstart-utr3_len:nstart]
                    else:
                        utr3 = record.seq[:nstart]
                    utr5 = utr5.reverse_complement()
                    utr3 = utr3.reverse_complement()
                    cds_seq = cds_seq.reverse_complement()
                    # pep = seq.translate()
                    print(record.id, feature.type, nstart, nend, strand, 'utr5', len(utr5), utr5)
                    print(record.id, feature.type, nstart, nend, strand, 'utr3', len(utr3), utr3)
            # else:
            #     print(feature.type)


if __name__ == '__main__':
    args = parse_args()
    acc_list = extract_taxonomy(args.taxonomy)
    print('#acc_list:',len(acc_list))
    # read_genebank(args.genbank, acc_list)
    parse_genebank(args.genbank, acc_list, args.legth5, args.length3)