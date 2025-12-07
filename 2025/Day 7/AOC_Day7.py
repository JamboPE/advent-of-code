# Advent of Code 2025 Day 7
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# Get the name of the current Python file
day = str(os.path.basename(__file__))[-4:-3]
year = str(os.path.dirname(__file__)).split("\\")[-2]

# Part A
with open(f"{year}/Day {day}/input","r") as input_file:
#with open(f"{year}/Day {day}/dev_input","r") as input_file:
   lines = input_file.readlines()
   input_file.close()

def print_list(list:list) -> None:
   print("")
   for entry in list:
      print(entry.replace("\n",""))

def partA():
   newLines = lines
   columnLength = len(lines[0])
   for columnIndex in range(0,columnLength):
      if lines[0][columnIndex] == "S":
         newLines[0] = str(newLines[0][:columnIndex])+"|"+str(newLines[0][columnIndex+1:])
   splits = 0
   for rowIndex in range(1,columnLength):
      for columnIndex in range(0,columnLength):
         if newLines[rowIndex-1][columnIndex] == "|":
            if newLines[rowIndex][columnIndex] == "^":
               newLines[rowIndex] = str(newLines[rowIndex][:columnIndex-1])+"|^|"+str(newLines[rowIndex][columnIndex+2:])
               splits += 1
            else:
               newLines[rowIndex] = str(newLines[rowIndex][:columnIndex])+"|"+str(newLines[rowIndex][columnIndex+1:])
   print_list(newLines)
   print(splits)

partA()