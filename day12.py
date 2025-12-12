#!/usr/bin/env python3
import numpy as np
from collections import defaultdict
from functools import lru_cache

f = open("2025/ressources/day12.txt", "r") #Open File
lines = f.readlines() #Separate in lines

# Part input
presents = list()
gridsizes = []
requirements = []
present = np.zeros((3,3))
presentindex = 0
presentnb = 0
for line in lines:
    line = line.replace("\n", "")
    if len(line) < 3:
        continue
    if "x" in line:
        line = line.replace("x", " ").replace(":", "")
        infos = line.split(" ")
        width, height = int(infos[0]), int(infos[1])
        gridsizes.append((width, height))
        requirements.append([int(x) for x in infos[2:]])
    else:
        line = line.replace(".", "0").replace("#", "1")
        present[presentindex, :] = [int(x) for x in line]
        presentindex += 1
        if presentindex == 3:
            presents.append(present.copy())
            presentindex = 0
        
# Q1
placeNeeded = []
for present in presents:
    placeNeeded.append(np.sum(present))

possible = np.zeros((1, len(gridsizes)))
i = 0
for gridsize, requirement in zip(gridsizes, requirements):
    gridArea = gridsize[0] * gridsize[1]
    presentArea = np.array(requirement) * np.array(placeNeeded)
    if np.sum(presentArea) <= gridArea:
        possible[0, i] = 1
    i += 1
print("The number of presents arrangements possible is", int(np.sum(possible)), "out of", len(gridsizes))

# Started to write the code before realizing the "trick"... disappointed
def flipH(present):
    return np.flip(present, axis=1)
def rotateL(present):
    return np.rot90(present, k=1)
def rotateR(present):
    return np.rot90(present, k=-1)
def rotate180(present):
    return np.rot90(present, k=2)

allpresents = defaultdict(list)
for i, present in enumerate(presents):
    allpresents[i].append(present)
    allpresents[i].append(rotateL(present))
    allpresents[i].append(rotateR(present))
    allpresents[i].append(rotate180(present))
    fh = flipH(present)
    allpresents[i].append(fh)
    allpresents[i].append(rotateL(fh))
    allpresents[i].append(rotateR(fh))
    allpresents[i].append(rotate180(fh))
    allpresents[i] = np.unique(allpresents[i], axis=0)

def canPlace(grid, present, x, y):
    ph, pw = present.shape
    gh, gw = grid.shape
    if x + pw > gw or y + ph > gh:
        return False
    gridpart = grid[y:y+ph, x:x+pw]
    overlap = gridpart + present
    if np.any(overlap > 1):
        return False
    return True

def place(grid, present, x, y):
    ph, pw = present.shape
    if canPlace(grid, present, x, y):
        newgrid = grid.copy()
        newgrid[y:y+ph, x:x+pw] += present
        return newgrid, True
    else:
        return grid, False