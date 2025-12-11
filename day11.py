#!/usr/bin/env python3
import numpy as np
from collections import defaultdict
from functools import lru_cache

f = open("2025/ressources/day11.txt", "r") #Open File
lines = f.readlines() #Separate in lines

# Parse Input
nodes = defaultdict(list)
for line in lines:
    line = line.replace("\n", "").replace(":", "")
    parts = line.split(" ")
    node = parts[0]
    connections = parts[1:]
    nodes[node] = list(connections)

# Q1
@lru_cache
def countPaths(start, end):
    if start == end:
        return 1
    totalPaths = 0
    for neighbor in nodes[start]:
        totalPaths += countPaths(neighbor, end)
    return totalPaths

nbPaths = countPaths("you", "out")
print("The total number of paths is:", nbPaths)

# Q2
nbPaths1 = countPaths("svr", "fft")
nbPaths2 = countPaths("fft", "dac")
nbPaths3 = countPaths("dac", "out")
totalPathsQ2 = nbPaths1 * nbPaths2 * nbPaths3

nbPaths1 = countPaths("svr", "dac")
nbPaths2 = countPaths("dac", "fft")
nbPaths3 = countPaths("fft", "out")
totalPathsQ2 += nbPaths1 * nbPaths2 * nbPaths3 # This is actually zero
print("The total number of paths is passing by dac and fft is:", totalPathsQ2)