"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.

# No setup
repeat forever:
    read input
    tokenize input
    if the first token is 'q'
        quit
    else
        decide which math function to call based on first token
"""

from arithmetic import *


# Your code goes here
while True:
    input_string = raw_input("> ")
    input_string = input_string.split(" ")
    if input_string[0] == 'q':
        print "Quitting calculator."
        break  # Quit the program?
    elif input_string[0] == "+":
        print add(int(input_string[1]), int(input_string[2]))
