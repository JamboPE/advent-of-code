# Advent of Code 2023 Day 3 Part A
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from AOC_utils import *

# Turn input file into a 2D array
def day3_input_to_array(input_filename):
    input_file = open(f"Day 3/{input_filename}","r")
    done = False
    input_array = []
    for line in input_file:
        line = line.replace("\n","")
        line_array = ['.']
        for char in line:
            line_array.append(char)
        line_array.append('.')
        if done == False:
            done = True
            buffer_line = []
            for i in range (0,len(line_array)):
                buffer_line.append('.')
            input_array.append(buffer_line)
        input_array.append(line_array)
    input_array.append(buffer_line)
    return input_array

input_file_array = day3_input_to_array("input")
for line in input_file_array:
    print(line)

not_symbols = ["0","1","2","3","4","5","6","7","8","9","."]
number_symbols = ["0","1","2","3","4","5","6","7","8","9"]

test = []
test2 = []
line_no = 0
for line in input_file_array:
    skip = 0
    char_no = 0
    for char in line:
        if skip > 0:
            skip -= 1
            pass
        elif char in number_symbols:
            i = 0
            test = []
            while line[char_no+i] in number_symbols:
                test.append(line[char_no+i])
                i += 1
            skip = i-1
            test2.append(test)
            if len(test) == 1:
                input_file_array[line_no][char_no] = ["1",char]
            if len(test) == 2:
                input_file_array[line_no][char_no] = ["2",char,line[char_no+1]]
                input_file_array[line_no][char_no+1] = ["X"]
            if len(test) == 3:
                input_file_array[line_no][char_no] = ["3",char,line[char_no+1],line[char_no+2]]
                input_file_array[line_no][char_no+1] = "X"
                input_file_array[line_no][char_no+2] = "X"
        char_no += 1
    line_no += 1

line_index = 0
engine = []
for line in input_file_array:
    char_index = 0
    for char in line:
        if isinstance(char, list) == False:
            pass
        elif char[0] == "1":
            if input_file_array[line_index-1][char_index-1] not in not_symbols or input_file_array[line_index-1][char_index] not in not_symbols or input_file_array[line_index-1][char_index+1] not in not_symbols or input_file_array[line_index][char_index-1] not in not_symbols or input_file_array[line_index][char_index+1] not in not_symbols or input_file_array[line_index+1][char_index-1] not in not_symbols or input_file_array[line_index+1][char_index] not in not_symbols or input_file_array[line_index+1][char_index+1] not in not_symbols:
                engine.append(f"{char[1]}")
        elif char[0] == "2":
            if input_file_array[line_index-1][char_index-1] not in not_symbols or input_file_array[line_index-1][char_index] not in not_symbols or input_file_array[line_index-1][char_index+1] not in not_symbols or input_file_array[line_index][char_index-1] not in not_symbols or input_file_array[line_index+1][char_index-1] not in not_symbols or input_file_array[line_index+1][char_index] not in not_symbols or input_file_array[line_index+1][char_index+1] not in not_symbols or input_file_array[line_index-1][char_index+2] not in not_symbols or input_file_array[line_index][char_index+2] not in not_symbols or input_file_array[line_index+1][char_index+2] not in not_symbols:
                engine.append(f"{char[1]}{char[2]}")
        elif char[0] == "3":
            if input_file_array[line_index-1][char_index-1] not in not_symbols or input_file_array[line_index-1][char_index] not in not_symbols or input_file_array[line_index-1][char_index+1] not in not_symbols or input_file_array[line_index][char_index-1] not in not_symbols or input_file_array[line_index+1][char_index-1] not in not_symbols or input_file_array[line_index+1][char_index] not in not_symbols or input_file_array[line_index+1][char_index+1] not in not_symbols or input_file_array[line_index-1][char_index+2] not in not_symbols or input_file_array[line_index+1][char_index+2] not in not_symbols or input_file_array[line_index-1][char_index+3] not in not_symbols or input_file_array[line_index][char_index+3] not in not_symbols or input_file_array[line_index+1][char_index+3] not in not_symbols:
                engine.append(f"{char[1]}{char[2]}{char[3]}")

        char_index += 1
    line_index += 1

print(engine)

engine_sum = 0
for entry in engine:
    engine_sum += int(entry)
print(engine_sum)

copy_to_clipboard(engine_sum)