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
    numbers_list = input_string[1:]
    if input_string[0] == 'q':
        print "Quitting calculator."
        break
    elif input_string[0] == "+":
        print reduce(add, numbers_list)
    elif input_string[0] == "-":
        print reduce(subtract, numbers_list)
    elif input_string[0] == "*":
        print reduce(multiply, numbers_list)
    elif input_string[0] == "/":
        print reduce(divide, numbers_list)
    elif input_string[0] == "square":
        print square(int(input_string[1]))
    elif input_string[0] == "cube":
        print cube(int(input_string[1]))
    elif input_string[0] == "pow":
        print reduce(power, numbers_list)
    elif input_string[0] == "mod" or "%":
        print reduce(mod, numbers_list)
