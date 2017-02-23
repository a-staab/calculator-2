# to be used with calculator file in calculator-2


def add(num1, num2):
    """Return the sum of two numbers"""
    return int(num1) + int(num2)


def subtract(num1, num2):
    """Return the difference of two numbers"""
    return int(num1) - int(num2)


def multiply(num1, num2):
    """Return the product of two numbers"""
    return int(num1) * int(num2)


def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return float(num1) / float(num2)


def square(num):
    """Return the square of a number"""
    return int(num[0]) ** 2


def cube(num):
    """Return the cube of a number"""
    return num ** 3


def power(num1, num2):
    """Return num raised to the power of exponent"""
    return int(num1) ** int(num2)


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return int(num1) % int(num2)


def my_reduce(user_function, user_list):
    while len(user_list) >= 2:
        new_first_item = user_function(user_list[0], user_list[1])
        print new_first_item
        user_list.pop(0)
        user_list[0] = new_first_item
        return user_list[0]
