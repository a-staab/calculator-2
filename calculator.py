"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.


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
    elif input_string[0] == "-":
        print subtract(int(input_string[1]), int(input_string[2]))
    elif input_string[0] == "*":
        print multiply(int(input_string[1]), int(input_string[2]))
    elif input_string[0] == "/":
        print divide(int(input_string[1]), int(input_string[2]))
    elif input_string[0] == "square":
        print square(int(input_string[1]))
    elif input_string[0] == "cube":
        print cube(int(input_string[1]))
    elif input_string[0] == "pow":
        print power(int(input_string[1]), int(input_string[2]))
    elif input_string[0] == "mod" or "%":
        print mod(int(input_string[1]), int(input_string[2]))