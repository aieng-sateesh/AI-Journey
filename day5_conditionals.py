# Day 5 - Python Conditionals Practice
# Author: Sateesh Kumar
# Date: 2025-05-05

# Q1: Check if a number is even or odd
def even_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

print(even_odd(7))


# Q2: Find the square of a number
def square_number(number):
    return number ** 2  # You can change to **3 for cube

print(square_number(4))


# Q3: Check if a number is a multiple of 5
def check_multiple_of_5(number):
    if number % 5 == 0:
        return 'Yes, it is a multiple of 5'
    else:
        return "No, it's not a multiple of 5"

print(check_multiple_of_5(42))


# Q4: Find absolute value of a number
def check_absolute_value():
    number = int(input('Enter a number:- '))
    if number < 0:
        return number * -1
    else:
        return number

print(check_absolute_value())


# Q5: Check if a number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return 'positive number.'
    elif number < 0:
        return 'negative number.'
    else:
        return 'zero'

print(check_number(0))


# Q6: Celsius to Fahrenheit converter
def C_to_F():
    C = float(input('Enter temperature in Celsius: '))
    F = ((9/5) * C) + 32
    print(f'Temp in Fahrenheit is {round(F, 2)}.')
    if C > 30:
        return '🔥 Hot'
    elif C < 15:
        return '❄️ Cold'
    else:
        return '🌤️ Moderate '

print(C_to_F())


# Q7: Check if a number is a perfect square
def check_square():
    number = int(input('Enter a number: '))
    for i in range(2, number):
        if number == i ** 2:
            return 'Perfect Square.'
    else:
        return 'Not a perfect square.'

print(check_square())
