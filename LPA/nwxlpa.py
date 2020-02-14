import networkx as nx
import csv
import matplotlib.pyplot as plt
from networkx.algorithms import community
import random

G = nx.Graph()

with open('/Users/cxy/Downloads/tgh/MengProgram2/pagerank/20180321.csv', 'r') as input_file:
    lines = csv.reader(input_file)
    for line in lines:
        G.add_edge(int(line[0]), int(line[1]))

def label_propagation_community(G):
    communities_generator = list(community.label_propagation_communities(G))
    m = []
    for i in communities_generator:
        m.append(list(i))
    return m

g=label_propagation_community(G)

for i in range(len(g)):
    c = lambda: random.randint(0,255)
    nx.draw(G, nodelist=g[i],node_color='#%02X%02X%02X'%(c(),c(),c()), node_size=1)
    
     
