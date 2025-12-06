#!/usr/bin/env python3
import numpy as np
from collections import defaultdict

f = open("2025/day6.txt", "r") #Open File
lines = f.readlines() #Separate in lines

# Parsing input
problems = defaultdict(list)

for line in lines:
    line = line.replace("\n", "")
    line = line.split()
    for i, number in enumerate(line):
        problems[i].append(number)

# Q1
total = 0
for problem in problems.values():
    sign = problem.pop()
    problem = [int(x) for x in problem]
    if sign == "+":
        result = np.sum(problem)
    if sign == "*":
        result = np.prod(problem)
    total += result

print("The total for Q1 is:", total)

# Q2
problems = defaultdict(list)

result=[]
data = np.zeros((len(lines)-1, len(lines[0])-1))
signs = []
for i, x in enumerate(lines[:-1]):
    line = x.replace("\n", "")
    values = list(line)
    values = [int(v) if v.isdigit() else -1 for v in values]
    data[i, :] = values
    
signs = [line for line in lines[-1].replace("\n", "").split()]

problems = defaultdict(list)

index = 0
for data_row in data.T:
    digits = data_row[data_row != -1]
    digits = digits.astype(int)
    digits = [str(d) for d in digits]
    digits = "".join(digits)
    if len(digits) > 0:
        problems[index].append(int(digits))
    else:
        index += 1

total = 0
for values, signs in zip(problems.values(), signs):
    if signs == "+":
        result = np.sum(values)
    if signs == "*":
        result = np.prod(values)
    total += result
print("The total for Q2 is:", total)       
