
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# Get the name of the current Python file
day = str(os.path.basename(__file__))[-4:-3]
year = str(os.path.dirname(__file__)).split("\\")[-2]

# Part A
#with open(f"{year}/Day {day}/input","r") as input_file:
with open(f"{year}/Day {day}/dev_input","r") as input_file:
   lines = input_file.readlines()
   input_file.close()