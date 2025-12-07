# Advent of Code 2025 Day 6
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

def partA():
   mathsArray = []
   for line in lines:
      if line.strip() == "":
         continue
      newLine = line
      while "  " in newLine:
         newLine = newLine.replace("  "," ")
      mathsArray.append(newLine.replace("\n","").strip().split(" "))

   length = len(mathsArray[0])
   for entry in mathsArray:
      if len(entry) != length:
         print(f"{entry} not the same length as {mathsArray[0]}")
         quit()

   totalSum = 0
   for i in range(0,len(mathsArray[0])):
      subTotal = int(mathsArray[0][i])
      if mathsArray[-1][i] == "+":
         for n in range (1,len(mathsArray)-1):
            subTotal += int(mathsArray[n][i])
      elif mathsArray[-1][i] == "-":
         for n in range (1,len(mathsArray)-1):
            subTotal -= int(mathsArray[n][i])
      elif mathsArray[-1][i] == "*":
         for n in range (1,len(mathsArray)-1):
            subTotal = subTotal * int(mathsArray[n][i])
      totalSum += subTotal
   print(totalSum)

partA()