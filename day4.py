#!/usr/bin/env python3
import numpy as np

f = open("2025/ressources/day4.txt", "r") #Open File
data = f.readlines() #Separate in lines

rolls = []
for line in data:
    line = line.replace("\n", "")
    line = line.replace(".", "0")
    line = line.replace("@", "1")
    rolls.append([int(x) for x in list(line)])

rolls = np.array(rolls)
rolls_positions = set()
for i in range(rolls.shape[0]):
    for j in range(rolls.shape[1]):
        if rolls[i, j] == 1:
            rolls_positions.add((i, j))

eight_neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

#Q1
total = 0
for roll in rolls_positions:
    i, j = roll
    neighbors = 0
    for di, dj in eight_neighbors:
        ni, nj = i + di, j + dj
        if (ni, nj) in rolls_positions:
            neighbors += 1
    if neighbors < 4:
        total += 1

print("The total number of safe rolls is: {}".format(total))

#Q2
removed = set()
removable = 1
while removable > 0:
    removable = 0
    for roll in rolls_positions.copy():
        i, j = roll
        neighbors = 0
        for di, dj in eight_neighbors:
            ni, nj = i + di, j + dj
            if (ni, nj) in rolls_positions:
                neighbors += 1
        if neighbors < 4:
            removable += 1
            removed.add((i, j))
            rolls_positions.remove((i, j))

print("The total number of removable rolls is: {}".format(len(removed)))