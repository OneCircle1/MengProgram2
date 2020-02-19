import pandas as pd
import numpy as np
import networkx as nx
import csv

node2index = {}
index2node = {}
G = {}

def PageRank(M, alpha, root):

    result = []
    n = len(M)
    v = np.zeros(n)
    v[node2index[root]] = 1
    while np.sum(abs(v - (alpha*np.matmul(M,v) + (1-alpha)*v))) > 0.0001:
        v = alpha * np.matmul(M, v) + (1-alpha)*v
    for ind, prob in enumerate(v):
        result.append((index2node[ind], prob))
    result = sorted(result, key=lambda x:x[1], reverse=True)[:num_candidates]
    return result

def Generate_Transfer_Matrix(G):
    """generate transfer matrix given graph"""
    index2node = dict()
    node2index = dict()
    for index,node in enumerate(G.keys()):
        node2index[node] = index
        index2node[index] = node
    # num of nodes
    n = len(node2index)
    # generate Transfer probability matrix M, shape of (n,n)
    M = np.zeros([n,n])
    for node1 in G.keys():
        for node2 in G[node1]:
            try:
                M[node2index[node2],node2index[node1]] = 1/len(G[node1])
            except:
                continue
    return M, node2index, index2node

# with open('20180321.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('20180321_new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         G = {rows[0]:rows[1] for rows in reader}

with open('20180321.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('20180321_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        for rows in reader:
            G.setdefault(rows[1],[]).append(rows[0])


print(G)

alpha = 0.85
root = '236274321'
# num_iter = 100
num_candidates = 10

M, node2index, index2node = Generate_Transfer_Matrix(G)
print(M)
result1 = PageRank(M, alpha, root)
print(pd.DataFrame(M, index=G.keys(), columns=G.keys()))
print(result1)

