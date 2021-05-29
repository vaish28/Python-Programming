# -*- coding: utf-8 -*-
"""
Six degrees of separation
"""

import networkx as nx
import numpy as np

G=nx.read_edgelist('facebook_combined.txt') # Read a graph from a list of edges, given in a file
N=list(G.nodes())   # get all pair of nodes from G and get in a list
# To find length of shortest path between each pair of nodes
shrtpath_lenlist=[]

for u in N:
    for v in N:
        if u!=v:
            length=nx.shortest_path_length(G,u,v)
            print("shorted path between", u, "and", v, "is of length:",length)
            shrtpath_lenlist.append(length)
            
min_shrtpath_len=min(shrtpath_lenlist)  
max_shrtpath_len=max(shrtpath_lenlist)
avg_shrtpath_len=np.average(shrtpath_lenlist) # use numpy module to find avg of a list

print("Minimum shortest path length:",min_shrtpath_len)
print("Maximum shortest path length:",max_shrtpath_len)
print("Average shortest path length:",avg_shrtpath_len)






