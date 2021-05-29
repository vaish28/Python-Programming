# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:10:33 2021

@author: User
"""
'''
import networkx as nx

gh = nx.Graph()

ls  = [1,2,3]

gh.add_nodes_from(ls)
gh.add_edge(1,2)
gh.add_edge(2,3)
gh.add_edge(1,3)


nx.draw(gh)
'''

import networkx as nx

#gh1 = nx.complete_graph(10)
#nx.draw(gh1)

gh2 = nx.gnp_random_graph(20,0.5)
nx.draw(gh2)