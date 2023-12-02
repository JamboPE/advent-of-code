# Advent of Code Day 1
import pyperclip

output_array = []
valid_numbers = ["1","2","3","4","5","6","7","8","9","0","one","two","three","four","five","six","seven","eight","nine"]
valid_numbers_lengths = []
for entry in valid_numbers:
    valid_numbers_lengths.append(len(entry))
file = open("input","r")

for line in file:
    line_numberised = []
    characters = []
    i = 0
    for character in line:
        characters.append(character)
        if character in valid_numbers[0:9]:
            line_numberised.append(valid_numbers[valid_numbers.index(character)])
        elif len(characters) < 3:
            pass
        else:
            if len(characters) >= 3:
                if str(characters[i-2])+str(characters[i-1])+str(characters[i]) == "one":
                    line_numberised.append("1")
                elif str(characters[i-2])+str(characters[i-1])+str(characters[i]) == "two":
                    line_numberised.append("2")
                elif str(characters[i-2])+str(characters[i-1])+str(characters[i]) == "six":
                    line_numberised.append("6")
            if len(characters) >= 4:
                if str(characters[i-3])+str(characters[i-2])+str(characters[i-1])+str(characters[i]) == "four":
                    line_numberised.append("4")
                elif str(characters[i-3])+str(characters[i-2])+str(characters[i-1])+str(characters[i]) == "five":
                    line_numberised.append("5")
                elif str(characters[i-3])+str(characters[i-2])+str(characters[i-1])+str(characters[i]) == "nine":
                    line_numberised.append("9")
            if len(characters) >= 5:
                if str(characters[i-4])+str(characters[i-3])+str(characters[i-2])+str(characters[i-1])+str(characters[i]) == "three":
                    line_numberised.append("3")
                elif str(characters[i-4])+str(characters[i-3])+str(characters[i-2])+str(characters[i-1])+str(characters[i]) == "seven":
                    line_numberised.append("7")
                elif str(characters[i-4])+str(characters[i-3])+str(characters[i-2])+str(characters[i-1])+str(characters[i]) == "eight":
                    line_numberised.append("8")
        i = i + 1
    output_array.append(int(str(line_numberised[0])+str(line_numberised[-1])))
sum = 0
for entry in output_array:
    sum = sum + entry
print(sum)
user = input("Copy to clipboard? [Y/n]")
if user != "" and user != "Y" and user != "y":
    print("Not copied")
else:
    try:
        pyperclip.copy(sum)
    except:
        print("Failed to copy to clipboard")
    else:
        print("Answer copied to clipboard")