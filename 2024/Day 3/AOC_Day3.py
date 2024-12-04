# Advent of Code 2024 Day 3
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
#

# Part A
with open("2024/Day 3/input","r") as input_file:
#with open("2024/Day 3/dev_inputB","r") as input_file:
    data = input_file.read()
    input_file.close()

total = 0
mulEnabled = True
for i in range(len(data)):
    if data[i:i+4] == "do()":
        mulEnabled = True
    elif data[i:i+6] == "don't(":
        mulEnabled = False
    if data[i:i+4] == "mul(":
        if "," not in data[i+4:]:
            break
        else:
            try:
                x = int(data[i+4:].split(",")[0])
            except:
                pass
            else:
                if ")" not in "".join(data[i+4:].split(",")[1:]):
                    break
                else:
                    try:
                        y = int("".join(data[i+4:].split(",")[1:]).split(")")[0])
                    except:
                        pass
                    else:
                        if mulEnabled:

                            total += x*y
print(f"[Part 1] Total: {total}")