# Advent of Code 2025 Day 1
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
#

with open("2025/Day 1/input","r") as input_file:
#with open("2025/Day 1/dev_input","r") as input_file:
    lines = input_file.readlines()
    input_file.close()

# Part A

def partA(lines):
    zeros = 0
    currentCombination = 50
    for line in lines:
        instruction = int(line.replace("R","").replace("L","-").strip())
        currentCombination += instruction
        while currentCombination > 99:
            currentCombination += -100
        while currentCombination < 0:
            currentCombination += 100
        if currentCombination == 0:
            zeros += 1
    return zeros

def partB1(lines):
    zeros = 0
    currentCombination = 50
    for line in lines:
        zerosThisTurn = 0
        #passGo = False
        instruction = int(line.replace("R","").replace("L","-").strip())
        previousCombination = currentCombination
        absolutepreviousCombination = currentCombination
        currentCombination += instruction
        #print(currentCombination)
        #firstTime = False
        while currentCombination > 99:
            currentCombination += -100
            if currentCombination != 0 and previousCombination != 0:
                previousCombination = currentCombination
            #print("CLICK (>99):", currentCombination)
                zeros += 1
                zerosThisTurn += 1
            #passGo = True
        #firstTime = False
        while currentCombination < 0:
            currentCombination += 100
            if currentCombination != 0 and previousCombination != 0:
                previousCombination = currentCombination
            #if previousCombination != 0 or firstTime:
                #print("CLICK (>99):", currentCombination)
                zeros += 1
                zerosThisTurn += 1
                #passGo = True
                #firstTime = True
        if currentCombination == 0: #and (passGo == False or instruction < -99 or instruction > 99):
            zeros += 1
            #print("CLICK (end 0):", currentCombination)
            zerosThisTurn += 1
        if True:
            if instruction <  -99 or instruction > 99:
                print("-----------------------------------------")
            if instruction > 0:
                instruction = "R" + str(instruction)
            elif instruction < 0:
                instruction = "L" + str(instruction)[1:]
            if zerosThisTurn != 0:
                print(f"{str(instruction)}: {absolutepreviousCombination} -> {currentCombination} ({zerosThisTurn})")
            else:
                print(f"{instruction}: {absolutepreviousCombination} -> {currentCombination}")
        #input("")
    return zeros

def partB(lines):
    zeros = 0
    currentCombination = 50
    for line in lines:
        zerosThisTurn = 0
        instruction = line.strip()
        if instruction[0] == "R":
            instruction = instruction[1:]
            for i in range(0,int(instruction)):
                currentCombination += 1
                if currentCombination == 100:
                    currentCombination = 0
                if currentCombination == 0:
                    zerosThisTurn += 1
        elif instruction[0] == "L":
            instruction = instruction[1:]
            for i in range(0,int(instruction)):
                currentCombination -= 1
                if currentCombination == -1:
                    currentCombination = 99
                if currentCombination == 0:
                    zerosThisTurn += 1
        else:
            print("ERROR, not L or R")
            quit()
        zeros += zerosThisTurn
    return zeros

#print("Part A:", partA(lines))
print("Part B:", partB(lines))