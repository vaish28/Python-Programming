# -*- coding: utf-8 -*-
"""

"""
import networkx as nx
#import random

G=nx.read_edgelist('facebook_combined.txt') # Read a graph from a list of edges, given in a file
N=list(G.nodes())
#print(random.choice(N))
print(N)
