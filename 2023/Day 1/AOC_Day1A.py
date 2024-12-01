# Advent of Code Day 1
output_array = []
input = open("input","r")
for line in input:
    line_numbers = []
    for character in line:
        try:
            line_numbers.append(int(character))
        except:
            pass
    line_number = int(str(line_numbers[0])+str(line_numbers[-1]))
    output_array.append(line_number)
sum = 0
for entry in output_array:
    sum = sum + entry
print(sum)