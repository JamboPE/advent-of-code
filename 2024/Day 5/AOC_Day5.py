# Advent of Code 2024 Day 5
# Import packages
import sys
import os
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
#

# Part A
rules = []
updates = []
with open("2024/Day 5/input","r") as input_file:
#with open("2024/Day 5/dev_inputA","r") as input_file:
    data = input_file.readlines()
    input_file.close()
for line in data:
    if "|" in line:
        rules.append(line.strip().split("|"))
    elif "," in line:
        updates.append(line.strip().split(","))

midTotal = 0
appearBefore = {}
appearAfter = {}
for rule in rules:
    appearBefore[rule[1]] = rule[0]
    appearAfter[rule[0]] = rule[1]

for update in updates:
    for i in range(len(update)):
        try:
            appearAfter[update[i]]
        except:
            pass
        else:
            try:
                if update.index(appearAfter[update[i]]) < i :
                    break
            except:
                pass
        try:
            appearBefore[update[i]]
        except:
            pass
        else:
            try:
                if update.find(appearBefore[update[i]]) > i:
                    break
            except:
                pass
        if i == len(update)-1:
            midTotal += int(update[math.floor(len(update) / 2)])
            print(", ".join(update))
    
print(f"[Part 1] Mid Total: {midTotal}")