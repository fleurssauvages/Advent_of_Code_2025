#!/usr/bin/env python3
import numpy as np

f = open("2025/ressources/day2.txt", "r") #Open File
data = f.readlines()[0] #Separate in lines

#Read Instructions
ranges = data.replace("\n", "").split(",")
starts = [int(r.split("-")[0]) for r in ranges]
ends = [int(r.split("-")[1]) for r in ranges]

#Q1
invalids = set()
for a, b in zip(starts, ends):
    stra, strb = str(a), str(b)
    mid = len(stra) // 2
    halfstring = stra[:mid]
    if len(halfstring) == 0:
        halfstring = "1"
    while int(halfstring * 2) <= b:
        if int(halfstring * 2) >= a:
            invalids.add(int(halfstring * 2))
        halfstring = str(int(halfstring) + 1)

total = np.sum(list(invalids))
print("The total of invalids is: {}".format(total))

#Q2
invalids = set()
for a, b in zip(starts, ends):
    stra, strb = str(a), str(b)
    for i in range(a, b+1):
        s = str(i)
        res = s in (s + s)[1:-1]
        if res: invalids.add(i)

total = np.sum(list(invalids))
print("The ACTUAL total of invalids is: {}".format(total))