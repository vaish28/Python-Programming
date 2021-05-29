# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:16:52 2021

@author: User
"""

import networkx as nx

gh = nx.Graph()

ls  = [4,5,6]

gh.add_nodes_from(ls)
gh.add_edge(4,5)
gh.add_edge(4,6)
gh.add_edge(5,6)

print(gh.nodes())
print(gh.edges())

color_map = []
for node in gh:
    color_map.append('cyan')

nx.draw(gh,node_color=color_map,with_labels=True)