# -*- coding: utf-8 -*-
"""
Created on Fri May 21 20:08:45 2021

@author: User
"""

import networkx as nx
import random
#to randomly select the node
#create a directed garph of nodes 10
import operator


G = nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)

#print(G.in_edges())

x =random.choice([i for i in range(G.number_of_nodes())]) # choose the random node X for 
# random walk in graph

dict_counter = {} # a counter for each node key is for each node number count the number of times the number is visited
# counter for each node key is node number;value is count value(visited) 
for i in range(G.number_of_nodes()):
    dict_counter[i] = 0
# initialize all the node count visits to zero
    
dict_counter[x] = dict_counter[x]+1 # increment counter of x as visited

for i in range(100000):
    # number of iterations 100000 for random walk which matches with nx pagerank values
    # with nx pagerank values
    list_n=list(G.neighbors(x))
    if len(list_n)==0:   # if x is a sink
        x=random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[x]=dict_counter[x]+1
    else:     
        x=random.choice(list_n)  # choose a node randomly from the neighbors of x
        dict_counter[x]=dict_counter[x]+1
        
p = nx.pagerank(G)

sorted_p=sorted(p.items(),key=operator.itemgetter(1)) # sorted the dict P by value
#itemgetter(0) then sort on keys
#itemgetter sort on values 
#right now values and ranks are something we are interested in 
sorted_rw=sorted(dict_counter.items(),key=operator.itemgetter(1)) # sorted the dict dict_counter
# by value
print(sorted_p)  # page pank results from nx
print('My random walk results: ',sorted_rw) # our page rank results



    