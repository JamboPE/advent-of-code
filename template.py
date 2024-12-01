
# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import pyperclip
def copy_to_clipboard(stuff):
    try:
        pyperclip.copy(stuff)
    except:
        print("Failed to copy to clipboard")
    else:
        print("Answer copied to clipboard")
#

with open("Year/Day X/dev_inputA","r") as input_file:
    input_file.close()


#copy_to_clipboard()