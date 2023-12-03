# Advent of Code 2023 Day 2 Part A
import input_file_decoder as inpt
import pyperclip

power_sum = 0

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
    power = sums[0] * sums[1] * sums[2]
    power_sum += power

print("Total ID is", power_sum)
try:
    pyperclip.copy(power_sum)
except:
    print("Failed to copy to clipboard")
else:
    print("Answer copied to clipboard")