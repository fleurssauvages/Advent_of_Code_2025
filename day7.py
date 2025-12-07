#!/usr/bin/env python3
import numpy as np
from collections import defaultdict

f = open("2025/day7.txt", "r") #Open File
lines = f.readlines() #Separate in lines

# Parsing
beams = list()
splitters = list()
mapLength, mapWidth = len(lines), len(lines[0].replace("\n", ""))
for i, line in enumerate(lines):
    line = line.replace("\n", "")
    chars = list(line)
    if "S" in chars:
        start = (i, chars.index("S"))
        beams.append(start)
    if "^" in chars:
        ind = np.where(np.array(chars) == "^")[0]
        for idx in ind:
            splitters.append( (i, idx) )

#Q1
splits = 0
timelines = set()
while len(beams) > 0:
    beam = beams.pop(0)
    newPosition = (beam[0]+1, beam[1])
    hasSplit = False
    if newPosition[0] < mapLength:
        if newPosition in splitters:
            newPosition1 = (beam[0]+1, beam[1]+1)
            newPosition2 = (beam[0]+1, beam[1]-1)
            if newPosition1[1] < mapWidth and newPosition1 not in beams:
                beams.append(newPosition1)
                hasSplit = True
            if newPosition2[1] >= 0 and newPosition2 not in beams:
                beams.append(newPosition2)
                hasSplit = True
        else:
            if newPosition not in beams:
                beams.append(newPosition)
    else:
        timelines.add(beam)
    if hasSplit:
        splits += 1
                
print("The number of splits is:", splits)

#Q2 We go from the bottom and sum timelines upwards for each splitter
nbTimelines = np.zeros((mapLength, mapWidth))
for pos in timelines:
    nbTimelines[pos] += 1
    
for i in range(mapLength-2, -1, -1):
    for j in range(mapWidth):
        if (i, j) in splitters:
            if j-1 >= 0:
                nbTimelines[i, j] += nbTimelines[i+1, j-1]
            if j+1 < mapWidth:
                nbTimelines[i, j] += nbTimelines[i+1, j+1]
        else:
            nbTimelines[i, j] += nbTimelines[i+1, j]
            
print("The number of timelines is:", int(nbTimelines[start]))