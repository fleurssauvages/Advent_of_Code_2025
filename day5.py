#!/usr/bin/env python3
import numpy as np

f = open("2025/ressources/day5.txt", "r") #Open File
data = f.readlines() #Separate in lines

# Parse input
starts = []
ends = []
fruits = set()

for line in data:
    line = line.replace("\n", "")
    if len(line) == 0:
        continue
    parts = line.split("-")
    if len(parts) == 2:
        start = int(parts[0])
        end = int(parts[1])
        starts.append(start)
        ends.append(end)
    if len(parts) == 1:
        fruits.add(int(parts[0]))

# Q1
fresh_fruits = 0
for fruit in fruits:
    for start, end in zip(starts, ends):
        if start <= fruit <= end:
            fresh_fruits += 1
            break

print("The total number of fresh fruits is: {}".format(fresh_fruits))

# Q2
def joinIntervals(intervals):
    # Sort intervals based on the start
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    # Iterate through intervals and merge overlapping ones
    for current in intervals[1:]:
        last = merged[-1] # Get the last merged interval
        if current[0] <= last[1]:  # Overlap
            merged[-1] = (last[0], max(last[1], current[1]))  # Merge
        else:
            merged.append(current)
    return merged

intervals = list(zip(starts, ends))
merged_intervals = joinIntervals(intervals)
total_covered = sum(end - start + 1 for start, end in merged_intervals)
print("The total number of covered fruits is: {}".format(total_covered))