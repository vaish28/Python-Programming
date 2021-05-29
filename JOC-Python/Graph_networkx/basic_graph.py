# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:45:59 2021

@author: User
"""
import networkx as nx

gh = nx.Graph()

gh.add_node('n1')
gh.add_node('n2')
gh.add_node('n3')
gh.add_edge('n1','n3')
gh.add_edge('n1','n2')
gh.add_edge('n2','n3')

print(gh.nodes)
print(gh.edges)

nx.draw(gh)
 