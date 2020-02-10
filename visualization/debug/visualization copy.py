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
    # if G.degree[nodelist[i]] == 1:
    if G.degree[nodelist[i]] <= 10:
        remove_list.append(nodelist[i])

# print(G.number_of_nodes())


G.remove_nodes_from(remove_list)

print("number of nodes ",G.number_of_nodes())

sub_graphs = nx.connected_component_subgraphs(G)
print(sub_graphs[0].nodes())

# #n gives the number of sub graphs
# n = len(sub_graphs)

# # you can now loop through all nodes in each sub graph
# for i in range(n):
#     print("Subgraph:", i, "consists of ",sub_graphs[i].nodes())

nx.draw(G, node_size = 1)
# plt.show()

# plt.savefig("20180321.png")
