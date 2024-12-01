from datetime import datetime
import os

current_day = datetime.now().day # Change this to the day you want to create
current_year = datetime.now().year

if datetime.now().hour < 5:
    current_day -= 1

directory = f"{current_year}/Day {current_day}"
python_file = directory + f"/AOC_Day{current_day}A.py"

def create_file(file_name):
    try:
        created_file = open(file_name, "x")
    except:
        print("Uhh boss,",file_name,"already exists")
        exit()
    created_file.close()

if datetime.now().month != 12 or current_day < 1 or current_day > 25:
    print("It's not Advent yet!")
    exit()

try:
    os.mkdir(directory)
except:
    print("Uhh boss,",directory,"already exists")
    exit()
create_file(python_file)
create_file(directory + "/dev_inputA")
create_file(directory + "/dev_inputB")

py_file = open(python_file, "w")
py_file.write(f"# Advent of Code 2023 Day {current_day} Part A")
template = open("template.py", "r")
py_file.write(template.read())
template.close()
py_file.close()

curl_file = open("curl_command", "r")
for line in curl_file:
    curl_command = str(line).replace("CHANGETHISONE",str(current_day)).replace("CHANGETHISDIRECTORY",directory)
os.system(curl_command)
curl_file.close()

print("Done!")