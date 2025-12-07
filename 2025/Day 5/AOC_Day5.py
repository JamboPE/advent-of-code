# Advent of Code 2025 Day 5
# Import packages
import sys
import os
from concurrent.futures import ThreadPoolExecutor
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# Get the name of the current Python file
day = str(os.path.basename(__file__))[-4:-3]
year = str(os.path.dirname(__file__)).split("\\")[-2]

global freshRange
freshRange = []

# Part A
#with open(f"{year}/Day {day}/input","r") as input_file:
with open(f"{year}/Day {day}/dev_input","r") as input_file:
   lines = input_file.readlines()
   input_file.close()

def get_range(line):
   for number in range(int(line.split("-")[0]),int(line.split("-")[1])+1):
      if number not in freshRange:
         freshRange.append(number)   

def partB1():
   with ThreadPoolExecutor(max_workers=190) as executor:
      for line in lines:
         if "-" in line:
            executor.submit(get_range, line)
   print(len(freshRange))

def partA():
   freshRanges = []
   IDs = []
   fresh = 0
   ## split ranges and IDs
   for line in lines:
      if line.strip() == "":
         continue
      if "-" in line:
         freshRanges.append([int(line.split("-")[0]), int(line.split("-")[1].strip())])
      else:
         IDs.append(int(line.strip()))

   for ID in IDs:
      print(ID)
      for freshRange in freshRanges:
         if ID >= freshRange[0] and ID <= freshRange[1]:
            fresh += 1
            break
   print(fresh)

def partB():
   freshRanges = []
   for line in lines:
      if "-" in line:
         freshRanges.append( [int(line.split("-")[0]) , int(line.split("-")[1].strip())] )
   numberOfFreshIDs = 0
   sortedRanges = []
   while len(sortedRanges) != len(freshRanges):
      lowestRange = [999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,1]
      for freshRange in freshRanges:
         if freshRange in sortedRanges:
            continue
         elif freshRange[0] < lowestRange[0]:
            lowestRange = freshRange
      sortedRanges.append(lowestRange)

   countedRanges = [sortedRanges[0]]
   sortedRanges.remove(sortedRanges[0])
   for sortedRange in sortedRanges:
      if sortedRange in countedRanges:
         continue
      
      for i in range(0,len(sortedRanges)):
         if sortedRanges[i][0] < countedRanges[-1][1]:
            sortedRanges[i][0] = countedRanges[-1][1]

      newRangeLength = [sortedRange[1] - sortedRange[0] , sortedRange, False]
      for countedRange in countedRanges:
         if sortedRange[0] > countedRange[0] and sortedRange[1] < countedRange [1]:
            continue
         if (countedRange[1] - sortedRange[0]) > 0 and (countedRange[1] - sortedRange[0]) < newRangeLength[0]:
            newRangeLength = [countedRange[1] - sortedRange[0] , [sortedRange[0],countedRange[1]] , sortedRange]
      countedRanges.append(newRangeLength[1])
      if newRangeLength[2] != False:
         sortedRanges.remove(newRangeLength[2])
      for entry in countedRanges:
         print(entry)
      print()

partB()