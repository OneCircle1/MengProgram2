import networkx as nx
import pandas as pd
import csv
import datetime
import operator


def edge_list_to_graph():
    """
    :return: Weighted graph, where each node represents an airport
    """
    filename = input('Enter a file name: ')
    df = pd.read_csv(filename, names=['node1', 'node2'])
    df.groupby('node1')['node2'].size()
    df['count'] =df.groupby('node1')['node2'].transform(pd.Series.value_counts)
    df = df.drop_duplicates(subset=['node1', 'node2'], take_last=True)
    matrix = df.drop_duplicates(subset=['node1', 'node2'], take_last=True)
    matrix.to_csv('temp/out.csv', sep=',', encoding='utf-8', header=True, index=False)
    with open("temp/out.csv") as f:
        next(f)
        graph = nx.read_edgelist(f, delimiter=",", data=[("count", float)], create_using=nx.DiGraph())

    return graph


def dictionary():
    """
    :return: A dictionary representation of a weighted graph
    """
    data_dict = {}
    with open('/Users/cxy/Downloads/tgh/MengProgram2/pagerank/20180321.csv', 'r') as data_file:
        data = csv.DictReader(data_file, delimiter=",")
        for row in data:
            item = data_dict.get(row["node2"], dict())
            item[row["node1"]] = int(row["count"])
            data_dict[row["node2"]] = item

    return data_dict

G = edge_list_to_graph()
# Out-degree vector - total number of flights from each airport
out_degree = nx.DiGraph.out_degree(G, weight='count')
graph = dictionary()
# Total number of nodes in a graph
all_nodes = G.nodes()
n = len(all_nodes)


def leaked_sum(ranks):
    """
    :param ranks:
    :return: leaked rank = sum the page rank of all the nodes having no outgoing edge,\
    then divide this sum by total number of nodes. Creates an effect of outgoing edges\
    from a node which has originally no outgoing edge.
    """
    leaked_rank = 0
    for key, value in out_degree.items():
        new_value = float(value)
        if new_value == 0.0:
            leaked_rank = leaked_rank + ranks[key]
    leaked_rank /= n

    return leaked_rank


def page_rank(damping_factor, threshold):
    """
    :param damping_factor:
    :param threshold:
    :return: Page rank value for each node, top 15 page ranks, total sum of page ranks.
    """

    # all 1/n vector
    ranks = {x: float(1) / n for x in all_nodes}
    # all zero vector
    zero_vector = {el: 0 for el in all_nodes}
    # Teleportation vector
    teleport = (1 - damping_factor)/ n
    # Iteration count
    time = 0
    flag = True
    while flag:
        # current_time = datetime.datetime.now().time()
        # print('Iteration________________________________________:', time + 1,'Time:', current_time)
        leakedsum=leaked_sum(ranks)
        time +=1
        for node in all_nodes:
            sum_pg=0
            if node in graph:
                for item in graph[node].keys():
                    if out_degree[item] is not None:
                        sum_pg += ranks[item] * graph[node][item] / out_degree[item]
            zero_vector[node]=damping_factor * (sum_pg + leakedsum)+ teleport
        new_ranks = zero_vector
        # check_rank = sum(new_ranks.itervalues())
        # print check_rank
        # stopping criteria:
        if time<threshold:
            ranks = new_ranks
        else:
            flag = False
        check_rank = sum(new_ranks.itervalues())
    print('Total PR sum:', check_rank)
    print(new_ranks)
    top_ranks = sorted(new_ranks.items(), key=operator.itemgetter(1))

    print(top_ranks[:-15:-1])
    return ranks, time


airports_page_rank = page_rank(0.85, 100)
