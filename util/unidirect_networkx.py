#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: unidirect_networkx.py
date: 2021/3/31 下午4:50
author: Sitao Zhu
mail: zhusitao1990@163.com
'''

import pandas as pd
import networkx as nx
from nxviz import CircosPlot
import matplotlib.pyplot as plt



def save_to_file(handle,kwargs):
    with open(handle,'w') as f:
        for gene,value in kwargs.items():
            out = ','.join([gene,str(value)])
            f.write(out+'\n')



Domains = dict()
# df = pd.read_csv('/Users/zhusitao/WuHanU/colleague/ZYL/edge_bidirect_uniq_r_geneid.txt',header=0,sep='\t')
df = pd.read_csv('./RBP_interaction_with_geneid.csv',header=0,sep='\t')

domain = pd.read_csv('/Users/zhusitao/WuHanU/colleague/ZYL/Domains.new',header=None,sep='\t')
domain.columns = ['d','g','i']
for i,item in domain.iterrows():
    Domains[item.g] = item.d

edge_list = []
for i,item in df[['A','B']].iterrows():
    u,v = item
    w = 1
    edge_list.append((u,v,w))

G = nx.Graph()
G2 = nx.DiGraph()
G.add_weighted_edges_from(edge_list)
G2.add_weighted_edges_from(edge_list)

# 给node设置属性的另一种方式
# node_list = []
# for node in G.nodes:
#     node_list.append((node,{'color':'red'}))
# G.add_nodes_from(node_list)

# 给节点设置特定的属性
for n, d in G.nodes(data=True):
    d["domain"] = Domains[n]
    d["color"] = 'red'


for n, d in G2.nodes(data=True):
    d["domain"] = Domains[n]
    d["color"] = 'red'

# 查看属性
# for n, d in G.nodes(data=True):
#     print(n,d)

# 查看边的属性
# print(nx.get_edge_attributes(G,'weight'))



# pos=nx.shell_layout(G)
# nx.draw_networkx(G,pos,font_size=5,
#                  with_labels=True,)
# nx.draw_networkx_nodes(G,pos,node_size=800,
#                        node_color='tomato')


c = CircosPlot(graph=G,node_labels=True,
               node_size=600,fontsize=3,
               node_label_layout="rotation",
               node_grouping="domain",
               node_color="domain",
               node_order="domain",
               group_legend=True,
               group_label_color=True,
               group_label_offset=2,
               figsize=(12, 12))

plt.legend(handles=c.legend_handles,
           loc='best',
           bbox_to_anchor=(1, 0., 0.5, 0.5),
           title="Domain",
           ncol=2,
           markerscale=0.5,
           borderpad=1,
           shadow=True,
           fancybox=True)

c.draw()
plt.show()

