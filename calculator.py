# https://github.com/tyler-ufl/lab10-TW-MO
# Partner 1: Tyler Whittlesey
# Partner 2: Michelle Ocon

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
def div(b, a):
    if b == 0: raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
def exp(a, b):
    return a ** b
def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(b, a)
