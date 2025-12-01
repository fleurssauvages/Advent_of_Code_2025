#!/usr/bin/env python3
import numpy as np

f = open("2025/ressources/day1.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
currentPosition = 50
positions = [currentPosition]

for instruction in lines:
    instruction = instruction.replace("\n", "")
    if len(instruction) < 2:
        continue
    direction = instruction[0]
    value = int(instruction[1:])
    positions.append(positions[-1] + (value if direction == "R" else -value))

counter = np.sum(np.array(positions) % 100 == 0)

print("The counter is: {}".format(counter))

#Q2
counter = 0
for a, b in zip(positions, positions[1:]):
    if b % 100 == 0:
        counter += 1 + abs(b-a) // 100
    elif a % 100 == 0:
        counter += abs(b-a) // 100
    else:
        counter += abs(b // 100 -a // 100)

print("The new counter is: {}".format(counter))