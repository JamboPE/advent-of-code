# Advent of Code 2024 Day 4
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
#

# Part A
#with open("2024/Day 4/input","r") as input_file:
data = []
with open("2024/Day 4/dev_inputA","r") as input_file:
    for line in input_file:
        data.append(line.strip())
    input_file.close()

def check_upper_left()