import networkx as nx
import csv
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edge(1,2)
G.add_edge(3,4)

# UG = G.to_undirected()

# sub_graphs = nx.connected_component_subgraphs(UG)

# #n gives the number of sub graphs
# n = len(sub_graphs)

# # you can now loop through all nodes in each sub graph
# for i in range(n):
#     print("Subgraph:", i, "consists of ",sub_graphs[i].nodes())

graphs = list(nx.connected_component_subgraphs(G))

remo = []

remo.append( i for i in graphs[0].nodes)
remo.append( i for i in graphs[1].nodes)
print(remo)

print(graphs[1].nodes)

nx.draw(graphs[1], node_size = 1)

print(len(graphs))

print(len(graphs[0].nodes))