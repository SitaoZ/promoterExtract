#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: generate_network.py
date: 2021/3/26 下午2:21
author: Sitao Zhu
mail: zhusitao1990@163.com
'''

import networkx as nx
from random import choice
import pandas as pd
import matplotlib.pyplot as plt
from nxviz import CircosPlot
from networkx.drawing.nx_agraph import graphviz_layout

df = pd.read_csv('NAP1.sif',header=None,sep='\t')
df.columns = ['A','I','B']


edge_list = []
for i,item in df[['A','B']].iterrows():
    u,v = item
    w = 1
    edge_list.append((u,v,{'weight':w}))

G = nx.Graph()
G.add_weighted_edges_from(edge_list)

# 给node设置属性的另一种方式
# node_list = []
# for node in G.nodes:
#     node_list.append((node,{'color':'red'}))
# G.add_nodes_from(node_list)

# 给节点设置特定的属性
for n, d in G.nodes(data=True):
    d["class"] = choice(["a", "b", "c", "d", "e"])
    d["color"] = 'red'
for n, d in G.nodes(data=True):
    print(n,d)

# G.add_nodes_from(node_list)


# print(G.nodes)
# print(G['AT2G35110']['AT4G27130']['weight'])


# pos=nx.shell_layout(G)

# nx.draw_networkx(G,pos,font_size=5,
#                  with_labels=True,)

# nx.draw_networkx_nodes(G,pos,node_size=800,
#                        node_color='tomato')


c = CircosPlot(graph=G,node_labels=True,
               node_size=600,fontsize=8,
               node_label_layout="rotation",
               node_grouping="class",
               node_color="class",
               node_order="class",
               group_label_color=True,
               group_label_offset=2)
# c.node_colors = ["skyblue" for node_color in c.node_colors]

c.draw()
plt.show()

