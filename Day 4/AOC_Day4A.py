# Advent of Code 2023 Day 4 Part A
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from AOC_utils import *
#
input_file = open("Day 4/input","r")

input_file_array = [] # 2D array "columns": [ int(card_no), array[winners], array[scratched] ]
for _line in input_file:
    _line = _line.replace("\n","")
    _line_array = _line.split(":")
    card_no = int(_line_array[0].replace("Card ",""))
    _numbers = _line_array[1].replace("  "," ").replace(" | ", "|").split("|")
    winners = _numbers[0][1:].split(" ")
    scratched = _numbers[1].split(" ")
    input_file_array.append([card_no, winners, scratched])
input_file.close()

total_score = 0
for _line in input_file_array:
    no_of_winners = -1
    for i in range(len(_line[2])):
        if _line[2][i] in _line[1]:
            no_of_winners += 1
    if no_of_winners == -1:
        card_score = 0
    else:
        card_score = 1
    while no_of_winners > 0:
        card_score = card_score * 2
        no_of_winners -= 1
    total_score += card_score

print(total_score)

copy_to_clipboard(total_score)