#
# A Python version of a Morse Code translator.
#
# Author: Dakota Kallas
# Date: April 21, 2021
#

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Paramaters: An English message
# Returns: The Morse Code translation of the English message
def encrypt(msg):
    # Variable to hold the encrypted message
    encrypted = ''

    # Goes through each letter in the message
    for letter in msg:
        if letter != ' ':
            # Translate each letter using the Dictonary of
            # Morse Code characters.
            encrypted += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # 2 spaces indicates different words
            encrypted += ' '

    return encrypted

# Paramaters: An Morse Code message
# Returns: The English translation of the Morse Code message
def decrypt(msg):
    # Set the msg to be final so program can
    # find the end of the message
    msg += ' '
  
    decrypted = ''
    citext = ''
    for letter in msg:
  
        # Checks for space
        if (letter != ' '):
  
            # Counter to keep track of spaces
            i = 0
  
            # Storing morse code of a single character
            citext += letter
        else:
            # 1 space indicates a new character
            i += 1
  
            # 2 spaces indicates a new word
            if i == 2 :
  
                 # Adding a space to separate words
                decrypted += ' '
            else:
  
                # Accessing the keys using their values
                decrypted += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
  
    return decrypted

# Parameters: None
# Returns: A message read in from the user
def get_msg():
    msg = input("Please enter the message to be translated: ")
    print("\nLanguages:")
    print("E - English\nM - Morse Code")

    # Ask the user what language their message is in until
    # a valid input is entered.
    valid = False
    while valid == False:
        mode = input("Enter the language is your message in: ")
        mode = mode.strip()
        if mode == 'M' or mode ==  'E':
            valid = True
        else:
            print("Invalid input.\n")

    # Determine how to translate the message
    if mode == 'M':
        # Check for a valid Morse input
        for char in msg.strip():
            if char != '.' and char != '-' and char != ' ':
                print("Invalid message provided.")
                exit()
        return decrypt(msg.upper())
    else:
        return encrypt(msg.upper())

# Hard-coded driver function to run the program
def main():
    print("Welcome to the Morse Code translator.")
    translated = get_msg()
    print("Translated Message: {}".format(translated))
  
# Executes the main function
if __name__ == '__main__':
    main()