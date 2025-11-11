"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        return math.sqrt(a)# raise ValueError if a < 0
    except ValueError as e:
        return f'Error: {e}'
def hypotenuse(a, b):
    try:
        return math.hypot(a, b) # can have negative nums
    except ValueError as e:
        return f'Error: {e}'

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        # assert a != 0, ZeroDivisionError
        return b / a # raise ZeroDivisionError if a == 0
    except ZeroDivisionError as e:
        return f'Error: {e}'

def log(a, b):
    try:
        # assert b > 0, ValueError
        return math.log(b, a)# use math library + raise ValueError
    except ValueError as e:
        return f'Error: {e}'

def exp(a, b):
    return a ** b