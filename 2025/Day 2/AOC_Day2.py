# Advent of Code 2025 Day 2
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Part A

def check_if_valid(id):
    #print("\n\n"+str(id))
    #print(len(str(id))//2)
    if len(str(id))%2 != 0:
        return True
    half = str(str(id)[:int(len(str(id))/2)])
    predicted = half+half
    if int(predicted) == int(id):
        return False
    return True
    
def partA():
    total = 0
    with open("2025/Day 2/input","r") as input_file:
    #with open("2025/Day 2/dev_input","r") as input_file:
        idRanges = "".join(input_file.readlines()).replace("\n","").strip().split(",")
        input_file.close()
    for idRange in idRanges:
        for id in range(int(idRange.split("-")[0]), int(idRange.split("-")[1])+1):
            if not check_if_valid(id):
                print(id)
                total += int(id)
    print(f"Total: {total}")

# Part B

def check_if_valid_partB(id):
    for i in range(1,(len(str(id))//2)+1):
        if len(str(id))%i != 0:
            #print(f"string length {i} isn't a factor of {len(str(id))}")
            continue
        timesItWouldNeedToRepeat = len(str(id))//i
        #print(f"Times to repeat: {timesItWouldNeedToRepeat}, string: {str(id)[:i]}, Full ID: {id}, i: {i}, Current character: {str(id)[i]}")
        predictedInvalidId = ""
        for repeats in range(0,timesItWouldNeedToRepeat):
            predictedInvalidId += str(id)[:i]
            #print(f"Repeat: {repeats}")
        #print(f"Predicted Id: {predictedInvalidId}, actual ID: {id}")
        if int(predictedInvalidId) == int(id):
            return False
    return True

def partB():
    total = 0
    with open("2025/Day 2/input","r") as input_file:
    #with open("2025/Day 2/dev_input","r") as input_file:
        idRanges = "".join(input_file.readlines()).replace("\n","").strip().split(",")
        input_file.close()
    for idRange in idRanges:
        for id in range(int(idRange.split("-")[0]), int(idRange.split("-")[1])+1):
            if not check_if_valid_partB(id):
                print(id)
                total += int(id)
    print(f"Total: {total}")

if __name__ == "__main__":
    partB()