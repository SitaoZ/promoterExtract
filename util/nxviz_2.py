#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: nxviz_2.py
date: 2021/3/26 下午8:59
author: Sitao Zhu
mail: zhusitao1990@163.com
'''

from random import choice

import matplotlib.pyplot as plt
import networkx as nx

from nxviz.plots import CircosPlot

G = nx.barbell_graph(m1=10, m2=3)
for n, d in G.nodes(data=True):
    d["class"] = choice(["a", "b", "c", "d", "e"])

c = CircosPlot(
    G,
    node_grouping="class",
    node_color="class",
    node_order="class",
    node_labels=True,
    group_label_position="middle",
    group_label_color=True,
    group_label_offset=2,
)
c.draw()
plt.show()