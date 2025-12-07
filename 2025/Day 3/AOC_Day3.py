# Advent of Code 2025 Day 3
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

def find_highest(numbers):
   highest = ["-1","False"]
   for i in range(len(numbers)):
      if int(numbers[i]) > int(highest[0]):
         highest = [numbers[i], i]
   return highest[0],highest[1]

def partA():
   total = 0 
   for line in lines:
      line = line.replace("\n","").strip()
      if line == "":
         continue
      firstNumber,firstIndex = find_highest(line[:-1])
      lastNumber,lastIndex = find_highest(line[firstIndex+1:])
      if firstNumber == "-1" or lastNumber == "-1" or firstIndex == "False" or lastIndex == "False":
         print(f"ERROR lol: {firstIndex} {firstNumber}, {lastIndex} {lastNumber}")
         quit()
      print(f"{line}    {firstNumber}{lastNumber}")
      total += int(str(firstNumber)+str(lastNumber))
   print(f"Total: {total}")


def partB():
   total = 0 
   for line in lines:
      line = line.replace("\n","").strip()
      if line == "":
         continue
      numbers = {}
      
      # Digit 1
      digit,digitIndex = find_highest(line[:-11])
      numbers[0] = (digit,digitIndex)
      if digit == "-1" or digitIndex == "False":
            print(f"ERROR lol: {digit} {digitIndex}")
            quit()
      number = str(digit)

      # Digit 2-11
      for i in range(1,11):
         #print(f"{numbers[i-1][1]+1}:{(-11+i)}  ->  {line[numbers[i-1][1]+1:(-11+i)]}")
         digit,digitIndex = find_highest(line[numbers[i-1][1]+1:(-11+i)])
         numbers[i] = (digit,numbers[i-1][1]+1+int(digitIndex))
         number += str(digit)
         if digit == "-1" or digitIndex == "False":
            print(f"ERROR lol with {i}: {digit} {digitIndex}    ~ so far {number}")
            quit()

      # Digit 12
      #print(f"{numbers[i-1][1]+1}:{(-11+i)}  ->  {line[numbers[i-1][1]+1:]}")
      digit,digitIndex = find_highest(line[numbers[i-1][1]+1:])
      numbers[i] = (digit,numbers[i-1][1]+1+int(digitIndex))
      number += str(digit)
      if digit == "-1" or digitIndex == "False":
         print(f"ERROR lol with {i}: {digit} {digitIndex}    ~ so far {number}")
         quit()

      print(f"{line}    {number}")
      total += int(number)
   print(f"Total: {total}")

partB()