# Advent of Code 2024 Day 1 Part A
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import pyperclip
def copy_to_clipboard(stuff):
    try:
        pyperclip.copy(stuff)
    except:
        print("Failed to copy to clipboard")
    else:
        print("Answer copied to clipboard")
output = []
#

with open("2024/Day 1/input","r") as input_file:
    leftList = []
    rightList = []
    for line in input_file:
        leftList.append(line.strip().split("   ")[0])
        rightList.append(line.strip().split("   ")[1])
    input_file.close()

# Part 1
sorted_lists = []
leftList.sort()
rightList.sort()
runningTotal = 0
for i in range(len(leftList)):
    sorted_lists.append([leftList[i],rightList[i]])
    runningTotal += abs(int(rightList[i])-int(leftList[i]))
output.append(f"[Part 1] Running Total: {runningTotal}")

# Part 2
simScore = 0
for entry in leftList:
    similatities = 0
    for entry2 in rightList:
        if entry == entry2:
            similatities += 1
    simScore += int(entry)*similatities

output.append(f"[Part 2] Score: {simScore}")

print("\n".join(output))