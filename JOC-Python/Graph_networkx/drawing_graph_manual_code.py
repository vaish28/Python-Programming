# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:44:01 2021

@author: User
"""

'''

import networkx as nx
G=nx.gnp_random_graph(5,0.5) 
# paras: nos of nodes and probability of edge creation
# as we run it again the graph will be different try this 3 to 4 times
#at probability 1, it is a complete graph

# this graph will be used in our page rank program
nx.draw(G)
'''

import networkx as nx
G = nx.DiGraph()
#Create an empty graph structure (a “null graph”) with no nodes and no edges.

# G can be grown in several ways.

# Nodes

#Add one node at a time
# Add the nodes from any container (a list, dict, set or even the lines 
# from a file or the nodes from another graph).

'''
G.add_node(1)

G.add_nodes_from([2, 3])
G.add_nodes_from(range(100, 110))

H = nx.path_graph(10)
#nx.draw(G)

#nx.draw(H)

G.add_nodes_from(H)
nx.draw(G)
'''

'''
G = nx.path_graph(3)

print(list(G.nodes))
print(list(G))
nx.draw(G)
'''
#rwturns outgoing edge neighbours
G.add_edge(1,2) 
G.add_edge(2,3)
list1 = G.neighbors(2)
print([n for n in G.neighbors(2)])
print([n for n in G.neighbors(1)])
print([n for n in G.neighbors(3)])

    
    