# Advent of Code 2023 Day 3 Part A
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) # Change the path to the parent directory to import custom packages
from AOC_utils import *

# Function to convert input file to a 2D array
def day3_input_to_array(input_filename):
    input_file = open(f"Day 3/{input_filename}","r")
    done = False
    input_array = []
    for line in input_file:
        line = line.replace("\n","")
        line_array = ['.']  # Add a boundary dot at the beginning of each line
        for char in line:
            line_array.append(char)  # Add each character to the line array
        line_array.append('.')  # Add a boundary dot at the end of each line
        if done == False:
            done = True
            buffer_line = []
            for i in range (0,len(line_array)):
                buffer_line.append('.')  # Create a buffer line of . character
            input_array.append(buffer_line)  # Add the buffer line as the first line of the input array
        input_array.append(line_array)  # Add each formatted line from the input file to the input array
    input_array.append(buffer_line)  # Add the buffer line as the last line of the input array
    return input_array


input_file_array = day3_input_to_array("input") # Run the function to convert the input file to a 2D array

not_symbols = ["0","1","2","3","4","5","6","7","8","9","."]
number_symbols = ["0","1","2","3","4","5","6","7","8","9"]


test = []  # Initialize an empty list to store the extracted numbers
test2 = []  # Initialize an empty list to store the extracted numbers as lists
line_no = 0

# Iterate over each line in the input file array
for line in input_file_array:
    skip = 0  
    char_no = 0
    # Iterate over each character in the line
    for char in line:
        if skip > 0:
            skip -= 1
            pass
        elif char in number_symbols:
            i = 0
            test = []
            # Extract the full number from the line
            while line[char_no+i] in number_symbols:
                test.append(line[char_no+i])
                i += 1
            skip = i-1
            test2.append(test)
            # Update the input file array by replacing each numbers' first digit with an array containing the length of the full number and the digits themselves then replace the remaining digits with "X"
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
gear_products_array = []
for line in input_file_array:
    char_index = 0
    for char in line:
        if char == '*': # Scan the input file array for each * character
            possible_gear = []
            # Check the neighboring elements for numbers
            # Only consider X's if the array containing its respective number is not in the search area
            if isinstance(input_file_array[line_index-1][char_index-1],  list) == True:
                possible_gear.append(input_file_array[line_index-1][char_index-1])
            elif input_file_array[line_index-1][char_index-1] == 'X':
                if isinstance(input_file_array[line_index-1][char_index-2],  list) == True:
                    possible_gear.append(input_file_array[line_index-1][char_index-2])
                elif isinstance(input_file_array[line_index-1][char_index-3],  list) == True:
                    possible_gear.append(input_file_array[line_index-1][char_index-3])
            if isinstance(input_file_array[line_index-1][char_index],  list) == True:
                possible_gear.append(input_file_array[line_index-1][char_index])
            if isinstance(input_file_array[line_index-1][char_index+1],  list) == True:
                possible_gear.append(input_file_array[line_index-1][char_index+1])
            if isinstance(input_file_array[line_index][char_index-1],  list) == True:
                possible_gear.append(input_file_array[line_index][char_index-1])
            elif input_file_array[line_index][char_index-1] == 'X':
                if isinstance(input_file_array[line_index][char_index-2],  list) == True:
                    possible_gear.append(input_file_array[line_index][char_index-2])
                elif isinstance(input_file_array[line_index][char_index-3],  list) == True:
                    possible_gear.append(input_file_array[line_index][char_index-3])
            if isinstance(input_file_array[line_index][char_index+1],  list) == True:
                possible_gear.append(input_file_array[line_index][char_index+1])
            if isinstance(input_file_array[line_index+1][char_index-1],  list) == True:
                possible_gear.append(input_file_array[line_index+1][char_index-1])
            elif input_file_array[line_index+1][char_index-1] == 'X':
                if isinstance(input_file_array[line_index+1][char_index-2],  list) == True:
                    possible_gear.append(input_file_array[line_index+1][char_index-2])
                elif isinstance(input_file_array[line_index+1][char_index-3],  list) == True:
                    possible_gear.append(input_file_array[line_index+1][char_index-3])
            if isinstance(input_file_array[line_index+1][char_index],  list) == True:
                possible_gear.append(input_file_array[line_index+1][char_index])
            if isinstance(input_file_array[line_index+1][char_index+1],  list) == True:
                possible_gear.append(input_file_array[line_index+1][char_index+1])
            
            # Check if there are more than two numbers near the * character
            if len(possible_gear) > 1:
                gear_product = 1
                gears = []
                # Extract the full numbers from the possible_gear list
                for entry in possible_gear:
                    if entry[0] == "1":
                        gears.append(f"{entry[1]}")
                    elif entry[0] == "2":
                        gears.append(f"{entry[1]}{entry[2]}")
                    elif entry[0] == "3":
                        gears.append(f"{entry[1]}{entry[2]}{entry[3]}")
                # Calculate the product of the gears
                for entry in gears:
                    gear_product = gear_product * int(entry)
                # Append the gear product to the gear_products_array
                gear_products_array.append(gear_product)

        char_index += 1
    line_index += 1

gear_sum = 0
for entry in gear_products_array:
    gear_sum += int(entry)
print(gear_sum)

copy_to_clipboard(gear_sum)