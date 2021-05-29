# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:00:26 2021

@author: User
"""
import networkx as nx

U=nx.Graph()  # undirected graph

G=nx.DiGraph()  # directed graph

G.nodes()

#G.add_nodes_from([0,1,2]) # from list; but if many nodes then manually entering not ok

G.add_nodes_from([i for i in range(5)])

print(G.nodes())
print(list(G))
print("edges",G.edges())
print(G.out_edges())
print(G.in_edges())
nx.draw(G)

G.add_edge(1,2) # add edge from 1 to 2 i.e. draw an edge with incoming line from node 1 to node 2
print("edges",G.edges())
print("edges",G.in_edges(1)) #in edge of node 1
print("edges",G.out_edges(1))#out edge of node 1
G.add_edge(0,3)
G.add_edge(2,3)
#G.add_edge(3,2)
G.add_edge(3,4)
G.add_edge(4,1)
print(list(G))
print(list(G.out_edges(2)))
print(list(G.out_edges(2)))
print(list(G.in_edges(2)))
print(list(G.out_edges(3)))

nx.draw(G,with_labels=True)
#label for the nodes

'''
>>> 1 in G  # check if node in graph
True
>>> [n for n in G if n < 3]  # iterate through nodes
[1, 2]
>>> len(G)  # number of nodes in graph
5
'''