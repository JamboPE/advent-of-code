# Advent of Code 2024 Day 2
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
#

#Part 1
#with open("2024/Day 2/dev_inputA","r") as input_file:
with open("2024/Day 2/input","r") as input_file:
    reports = input_file.readlines()
    input_file.close()

def decending(line):
    line = line.split(" ")
    for index in range(1,len(line)):
        if int(line[index-1]) - int(line[index]) > 0 and int(line[index-1]) - int(line[index]) < 4:
            pass
        else:
            return "False"
    return "True"

def ascending(line):
    line = line.split(" ")
    for index in range(1,len(line)):
        if int(line[index-1]) - int(line[index]) < 0 and int(line[index-1]) - int(line[index]) > -4:
            pass
        else:
            return "False"
    return "True"

safe = 0
for report in reports:
    if decending(report) == "True" or ascending(report) == "True":
        safe += 1

print(f"[Part 1] Safe: {safe}")


#Part 2
#with open("2024/Day 2/dev_inputA","r") as input_file:
with open("2024/Day 2/input","r") as input_file:
    reports = input_file.readlines()
    input_file.close()

def decending(line):
    for index in range(1,len(line)):
        if int(line[index-1]) - int(line[index]) > 0 and int(line[index-1]) - int(line[index]) < 4:
            pass
        else:
            return "False"
    return "True"

def ascending(line):
    for index in range(1,len(line)):
        if int(line[index-1]) - int(line[index]) < 0 and int(line[index-1]) - int(line[index]) > -4:
            pass
        else:
            return "False"
    return "True"

def get_arrays_from_line(lineArray):
    array = [lineArray]
    for i in range (0,len(lineArray)):
        iterationArray = lineArray[:i] + lineArray[i+1:]
        array.append(iterationArray)
    return array

safe = 0
for report in reports:
    report = report.replace("\n","").strip().split(" ")
    reportCombinations = get_arrays_from_line(report)
    for reportCombination in reportCombinations:
        if decending(reportCombination) == "True" or ascending(reportCombination) == "True":
            safe += 1
            break
        

print(f"[Part 2] Safe: {safe}")