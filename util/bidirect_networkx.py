#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: bidirect_networkx.py
date: 2021/3/26 下午9:18
author: Sitao Zhu
mail: zhusitao1990@163.com
'''

#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: generate_network.py
date: 2021/3/26 下午2:21
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
df = pd.read_csv('./edge_bidirect_uniq_r_geneid_remove_outlier5.txt',header=0,sep='\t')

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


# c = CircosPlot(graph=G,node_labels=True,
#                node_size=600,fontsize=8,
#                node_label_layout="rotation",
#                node_grouping="domain",
#                node_color="domain",
#                node_order="domain",
#                group_legend=True,
#                group_label_color=True,
#                group_label_offset=2,
#                figsize=(12, 12))

# plt.legend(handles=c.legend_handles,
#            loc='best',
#            bbox_to_anchor=(1, 0., 0.5, 0.5),
#            title="Domain",
#            ncol=2,
#            markerscale=0.5,
#            borderpad=1,
#            shadow=True,
#            fancybox=True)

# c.draw()
#plt.show()


# degree centrality
from networkx import degree_centrality
from networkx import betweenness_centrality
from networkx import eigenvector_centrality
from networkx import articulation_points
from networkx import pagerank
from networkx import stochastic_graph
from networkx import closeness_centrality
from networkx import current_flow_closeness_centrality
from networkx import information_centrality
from networkx.algorithms import community


# step 1
print(degree_centrality(G))
# step 2
# print(betweenness_centrality(G))
# step 3
# print(eigenvector_centrality(G))
# step 4
# print(list(articulation_points(G)))
# step 5 different from igraph
# print(pagerank(G,alpha=0.85))
# step 6 different from igraph
closeness = nx.clustering(G)
save_to_file('closeness.txt',closeness)
# step7 information_centrality
print('information_centrality:',information_centrality(G))

print(nx.is_connected(G))
# community
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
print(sorted(map(sorted, next_level_communities)))
print(nx.info(G))
print(G2.is_directed())
print(G.is_directed())

import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

# module install
# pip install python-louvain
# compute the best partition
# 分组
partition = community_louvain.best_partition(G)
print('partition :',partition)
# draw the graph
pos = nx.spiral_layout(G)
# pos = nx.circular_layout(G)
nx.draw_networkx(G,pos,font_size=5,with_labels=False)
# color the nodes according to their partition 获取颜色
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
# 画出每一个分组的节点，设置大小，颜色
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()



# k shell decomposition
from networkx import k_shell,k_core
G.remove_edges_from(nx.selfloop_edges(G))
ks = k_shell(G, k=2)  #
print('ks:',ks.nodes())

kc = k_core(G, k=3)
print('kc:',kc.nodes())

pos = nx.spiral_layout(G)
nx.draw_networkx(G,pos=pos,with_labels=False)
plt.show()