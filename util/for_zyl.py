#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: for_zyl.py
date: 2021/3/30 下午2:56
author: Sitao Zhu
mail: zhusitao1990@163.com
'''

import pandas as pd

df =  pd.read_csv('zyl.sif',sep='\t',header=None)

df.columns = ['A','I','B']

#
# df_add = pd.read_csv('add.txt',header=None,sep='\t')
# df_add.columns = ['A','B','Desc']



first_layer = []
second_layer = []

for n,item in df.iterrows():
    if 'AT2G35110' in item.values.tolist():
        if item.A == 'AT2G35110':
            first_layer.append((item.A,item.B))
        else:
            first_layer.append((item.B, item.A))
    else:
        second_layer.append((item.A,item.B))


# for n,item in df_add.iterrows():
#     if 'AT2G35110' in item.values.tolist():
#         if item.A == 'AT2G35110':
#             first_layer.append((item.A,item.B))
#         else:
#             first_layer.append((item.B, item.A))


link = []
for inter in first_layer:
    link.append(inter[1])

second_layer_format = []
for inter in second_layer:
    if inter[0] in link:
        # 第一位
        second_layer_format.append(inter)
    elif inter[1] in link :
        # 第二位
        second_layer_format.append(inter[::-1])


# DESC
desc = pd.read_csv('~/Desktop/RBP/Arabidopsis_all_anno_20210128.txt',sep='\t',header=0)
# print(desc.columns)
sub_set = desc[['Gene ID','TAIR description']]

desc_dict = dict()

for n,item in sub_set.iterrows():
    desc_dict[item['Gene ID']] = item['TAIR description']

print(*['NAP1','first','second','first describe','second describe'],sep='\t')
for i in link:
    for g in second_layer_format:
        if i == g[0]:
            print(*['AT2G35110',i,g[1],desc_dict[i],desc_dict[g[1]]],sep='\t')



