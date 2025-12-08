#!/usr/bin/env python3
import numpy as np
from collections import defaultdict
import scipy.spatial as sp
import networkx as nx

f = open("2025/ressources/day8.txt", "r") #Open File
lines = f.readlines() #Separate in lines

boxes = list()
for line in lines:
    line = line.replace("\n", "")
    parts = line.split(",")
    x, y, z = parts[0], parts[1], parts[2]
    box_id = (int(x), int(y), int(z))
    boxes.append(box_id)

# Q1
distances = sp.distance_matrix(boxes, boxes) + np.eye(len(boxes)) * 1e12
indexes = [(i, j) for i in range(len(boxes)) for j in range(len(boxes))]
distances = list(np.ravel(distances, order='C'))
distances, indexes = zip(*sorted(zip(distances, indexes)))

n_junctions = 1000
graph = nx.Graph()
for i in range(n_junctions):
    box1, box2 = indexes[i*2]
    graph.add_edge(box1, box2)

subgraphs = nx.connected_components(graph)
subgraphs_len = [len(c) for c in sorted(subgraphs, key=len, reverse=True)]

n_largest = 3
n_biggest = np.prod(subgraphs_len[:n_largest])

print("The product of the sizes of the {} largest clusters is: {}".format(n_largest, n_biggest))

# Q2
i = n_junctions
while True:
    box1, box2 = indexes[i*2]
    graph.add_edge(box1, box2)
    subgraphs = [len(c) for c in sorted(nx.connected_components(graph), key=len, reverse=True)]
    if subgraphs[0] == len(boxes):
        break
    i += 1

print("The last cable needed: {}".format(boxes[box1][0]*boxes[box2][0]))