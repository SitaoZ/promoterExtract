#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: calculate_molecular_weight.py
date: 2021/3/31 下午3:46
author: Sitao Zhu
mail: zhusitao1990@163.com
'''

import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils.ProtParam import ProteinAnalysis



def transcript_to_dict(fasta_path):
    transcript_dict = dict()
    with open(fasta_path,'r') as handle:
        for record in SeqIO.parse(handle,'fasta'):
            trans_id = record.id.replace('transcript:','')
            trans_seq = record.seq
            transcript_dict[trans_id] = trans_seq
    return transcript_dict

def translate(trans_id):
    '''
    tranlste dna to aa
    :param trans_id: Seq object
    :return: aa
    '''
    conding_dna = trans_id
    aa_seq = conding_dna.translate(to_stop=True)
    return aa_seq

def molecular_weight(aa):
    x = ProteinAnalysis(aa)
    mw = "%0.2f" % x.molecular_weight()
    return mw

def main():
    transcript = pd.read_csv('~/Desktop/RBP/tobacco/repository_from_guilong/RBP_interaction_protein_location.csv', sep='\t', header=None)
    transcript.columns = ['index', 'trans_id', 'domain']
    transcript_dict = transcript_to_dict('CDS.fa')
    for n,item in transcript.iterrows():
        trans_id = item.trans_id
        # print(trans_id)
        trans_seq = transcript_dict[trans_id]
        aa_seq = translate(trans_seq)
        aa_seq = str(aa_seq)
        print(*[trans_id,str(molecular_weight(aa_seq))],sep='\t')

if __name__=='__main__':
    main()

