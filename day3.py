#!/usr/bin/env python3
import numpy as np

f = open("2025/ressources/day3.txt", "r") #Open File
data = f.readlines() #Separate in lines

def findbanks(line, n):
    lists = list(line)
    availableBanks = [int(x) for x in lists]
    string = ""
    for i in range(n, 0, -1):
        index = np.argmax(availableBanks[:len(availableBanks)-i+1])
        string += str(availableBanks[index])
        availableBanks = availableBanks[index+1:]
    bank = int(string)
    return bank

#Q1
banks = 0
for line in data:
    line = line.replace("\n", "")
    banks += findbanks(line, 2)

print("The total power banks is: {}".format(banks))

#Q2
banks = 0
for line in data:
    line = line.replace("\n", "")
    banks += findbanks(line, 12)

print("The new total power banks is: {}".format(banks))