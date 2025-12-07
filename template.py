
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# Get the name of the current Python file
day = str(os.path.basename(__file__))[-4:-3]
year = str(os.path.dirname(__file__)).split("\\")[-2]

option = input("""What input file should I use?
0: dev_input
1: input
Option (0/1): """)
if option == "1":
   inputFile = f"{year}/Day {day}/input"
else:
   inputFile = f"{year}/Day {day}/dev_input"

with open(inputFile,"r") as input_file:
   lines = input_file.readlines()
   input_file.close()

# Part A
def partA():
   for line in lines:
      print(line)

partA()