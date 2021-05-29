# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 08:50:57 2021

@author: Supriya
"""
import networkx as nx
#import random

G=nx.read_edgelist('facebook_combined.txt') # Read a graph from a list of edges, given in a file
N=list(G.nodes())
#print(random.choice(N))
print(N)