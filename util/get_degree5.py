#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: get_degree5.py
date: 2021/3/30 下午8:41
author: Sitao Zhu
mail: zhusitao1990@163.com
'''

import pandas as pd
from collections import defaultdict

df = pd.read_csv('edge_bidirect_uniq_r_geneid.txt',sep='\t',header=0)
dd = defaultdict(list)

for n,item in df.iterrows():
    A,B = item.A,item.B
    dd[A].append(B)
    dd[B].append(A)

for gene in dd.keys():
    set1 = set(dd[gene])
    if len(set1) > 5:
        list1 = list(set1)
        print(*[gene,','.join(list1)],sep='\t')
