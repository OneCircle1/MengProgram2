import networkx as nx
import csv
import matplotlib.pyplot as plt

G = nx.Graph()
with open('ds.csv', 'r') as input_file:
    lines = csv.reader(input_file)
    for line in lines:
        G.add_edge(int(line[0]), int(line[1]))

# use pagerank to ranking the nodes in the graph
pr = nx.pagerank(G, alpha = 0.9)
sorted_pr = [(k,v) for k, v in sorted(pr.items(), key = lambda item:item[1], reverse = True)]

# print the toppest 20 nodes
key_node_num = 20
for i in range (key_node_num):
    print(str(sorted_pr[i][0]).ljust(10, " "), "%.10f"%sorted_pr[i][1] )
