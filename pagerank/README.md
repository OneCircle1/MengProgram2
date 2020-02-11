# Page Rank
Find the key nodes using [pagerank algorithm](https://en.wikipedia.org/wiki/PageRank).
In [nextworkx document](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html), pagerank analysis can be used in an easy way. Even though it is an old document, the codes introduced there still works well.

# Instruction
Install python3.

Install networkx and matplotlib.

Run nwkxpgrk.py.

# Result
The key is the node and the value is the pagerank value. The nodes with top 5 pr value are shown as below.  
```
[(303207760, 0.002064974982357374), (236274321, 0.002051236035584388), (4330660, 0.0017084371041040385), (39819088, 0.0012231166082177169), (11168597, 0.0012083176973727275)]
```

Since we don't know which colume is the head in the csv file. I reverse the head and tail and calculae the pagerank again. The result is shown as below.  
```
[(303207760, 0.002265352213482891), (236274321, 0.002010489006453749), (4330660, 0.0018910901732115167), (11168597, 0.0011830686750502466), (39819088, 0.0011001224081980633)]
```

The directed graph visualization, where the node size is 1.  
![image](https://github.com/OneCircle1/MengProgram2/blob/master/pagerank/png/sz1.png)

The directed graph visualization, where the node size is linear with its pr value.  
![image](https://github.com/OneCircle1/MengProgram2/blob/master/pagerank/png/sz500.png)

The directed graph visualization after reversing the head and tail, where the node size is linear with its pr value.  
![image](https://github.com/OneCircle1/MengProgram2/blob/master/pagerank/png/sz500r.png)

# TODO
Write the algorithm using numpy.

# Question
How can we make use of pagerank in real life and what's the meaning of this csv file.
