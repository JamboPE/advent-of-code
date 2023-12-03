import os
import pyperclip

def copy_to_clipboard(stuff):
    try:
        pyperclip.copy(stuff)
    except:
        print("Failed to copy to clipboard")
    else:
        print("Answer copied to clipboard")