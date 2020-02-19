# Page Rank
Find the key nodes using [pagerank algorithm](https://en.wikipedia.org/wiki/PageRank).
In [nextworkx document](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html), pagerank analysis can be used in an easy way. Even though it is an old document, the codes introduced there still works well.

# Instruction
Install python3.

Install networkx and matplotlib.

Run nwkxpgrk.py.

# Result

The top 10 pr value created by .
```
[8284 rows x 8284 columns]
[('275995436', 0.019466309905308385), ('476410313', 0.01946381594026822), ('809524687', 0.01600534103045328), ('390148878', 0.016003042960857406), ('249422639', 0.011717182749134037), ('123570525', 0.009844364953666397), ('947272756', 0.008573799682473652), ('676285306', 0.008572709691425888), ('317866087', 0.005860695552687871), ('272834362', 0.005857889789848505)]
```


The directed graph visualization, where the node size is 1.  
![image](https://github.com/OneCircle1/MengProgram2/blob/master/pagerank/png/sz1.png)

The directed graph visualization, where the node size is linear with its pr value.  
![image](https://github.com/OneCircle1/MengProgram2/blob/master/pagerank/png/sz500.png)

The directed graph visualization after reversing the head and tail, where the node size is linear with its pr value.  
![image](https://github.com/OneCircle1/MengProgram2/blob/master/pagerank/png/sz500r.png)

# TODO
～～Write the algorithm using numpy.～～

# Question
How can we make use of pagerank in real life and what's the meaning of this csv file.
