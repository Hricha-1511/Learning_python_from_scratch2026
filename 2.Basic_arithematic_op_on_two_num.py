# Using user defined functions to perform the basic arithematic operations like sum , substract, multiplication , division , modulo division.

# code to perform basic arithmetic operations

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2


print(add(2, 1))
print(subtract(2, 1))
print(multiply(2, 1))
print(divide(5, 3))




