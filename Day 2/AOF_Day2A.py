# Advent of Code 2023 Day 2 Part A
import input_file_decoder as inpt
import pyperclip

requsted_cubes = [12,13,14]
id_total = 0

for game in inpt.convert_to_list("input"):
    game_no = game[0]
    sums = []
    red_sum = []
    green_sun = []
    blue_sum = []
    for round in range(len(game[1])):
        red_sum.append(int(game[1][round][0]))
        green_sun.append(int(game[1][round][1]))
        blue_sum.append(int(game[1][round][2]))
    sums.insert(0,max(red_sum))
    sums.insert(1,max(green_sun))
    sums.insert(2,max(blue_sum))
    debug = ""
    if sums[0] <= requsted_cubes[0] and sums[1] <= requsted_cubes[1] and sums[2] <= requsted_cubes[2]:
        id_total += game_no
        debug = "Selected"
    print(game_no,sums, debug)
    print("")
print("Total ID is", id_total)
try:
    pyperclip.copy(id_total)
except:
    print("Failed to copy to clipboard")
else:
    print("Answer copied to clipboard")