# Advent of Code 2025 Day 4
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# Get the name of the current Python file
day = str(os.path.basename(__file__))[-4:-3]
year = str(os.path.dirname(__file__)).split("\\")[-2]

# Part A
def get_array():
   with open(f"{year}/Day {day}/input","r") as input_file:
   #with open(f"{year}/Day {day}/dev_input","r") as input_file:
      lines = input_file.readlines()
      input_file.close()

   # Create initial row
   arrayLine = []
   for i in range (0,len(lines[0].replace("\n","").strip())+2):
      arrayLine.append(".")
   array = [arrayLine]

   # add lines from input with buffer column on each side
   for line in lines:
      line = line.replace("\n","").strip()
      arrayLine = ["."]
      for character in line:
         arrayLine.append(character)
      arrayLine.append(".")
      array.append(arrayLine)

   # Add final buffer row
   array.append(array[0])

   return array

def partA():
   array = get_array()
   accessibleRolls = 0
   for rowIndex in range(1,len(array)-1):
      for columnIndex in range(1,len(array[rowIndex])-1):
         filledSpaces = 0
         emptySpaces = 0
         if array[rowIndex][columnIndex] != "@":
            continue
         for i in range(-1,2):
            for n in range(-1,2):
               if i == 0 and n == 0:
                  continue
               elif array[rowIndex+i][columnIndex+n] == "@":
                  filledSpaces += 1
               elif array[rowIndex+i][columnIndex+n] == ".":
                  emptySpaces += 1
               else:
                  print("Error")
                  quit()
                  
         print(f"Current coordinate ({columnIndex},{rowIndex}), number of filled spaces: {filledSpaces}, empty: {emptySpaces}")
         if filledSpaces < 4:
            accessibleRolls += 1
   print(accessibleRolls)

# Part B

def partB():
   array = get_array()
   accessibleRolls = 0
   prevRolls = -1
   while prevRolls != accessibleRolls:
      prevRolls = accessibleRolls
      for rowIndex in range(1,len(array)-1):
         for columnIndex in range(1,len(array[rowIndex])-1):
            filledSpaces = 0
            emptySpaces = 0
            if array[rowIndex][columnIndex] != "@":
               continue
            for i in range(-1,2):
               for n in range(-1,2):
                  if i == 0 and n == 0:
                     continue
                  elif array[rowIndex+i][columnIndex+n] == "@":
                     filledSpaces += 1
                  elif array[rowIndex+i][columnIndex+n] == ".":
                     emptySpaces += 1
                  else:
                     print("Error")
                     quit()
                     
            print(f"Current coordinate ({columnIndex},{rowIndex}), number of filled spaces: {filledSpaces}, empty: {emptySpaces}")
            if filledSpaces < 4:
               accessibleRolls += 1
               array[rowIndex][columnIndex] = "."
   print(accessibleRolls)

partB()