import os
import networkx as nx

import matplotlib.pyplot as plt

import csv

G = nx.DiGraph()

with open('/Users/cxy/Downloads/tgh/MengProgram2/pagerank/20180321.csv', 'r') as input_file:
    lines = csv.reader(input_file)
    for line in lines:
        G.add_edge(int(line[0]), int(line[1]))

pr=nx.pagerank(G,alpha=0.85)

sortedpr = newA = dict(sorted(pr.items(), key=lambda x: x[1], reverse=True)[:5])

print(list(sortedpr.items()))


