import networkx as nx
import csv
import matplotlib.pyplot as plt

G = nx.Graph()

with open('20180321.csv', 'r') as input_file:
    lines = csv.reader(input_file)
    for line in lines:
        G.add_edge(int(line[0]), int(line[1]))

# Find and remove the nodes with only one degree
nodelist = [n for n in G.nodes]
remove_list = []
for i in range(len(nodelist)):
    if G.degree[nodelist[i]] == 1:
        remove_list.append(nodelist[i])
G.remove_nodes_from(remove_list)

nx.draw(G, node_size = 1)
plt.show()
