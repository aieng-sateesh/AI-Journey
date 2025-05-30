# Day 25 - Python Code Review Summary

# check even or odd
def check_even(n):
    if n % 2 == 0:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')

check_even(5)

# convert celsius to fahrenheit
def c_to_f(c):
    f = (c * 9/5) + 32
    print(f'{c}°C is {f}°F')

c_to_f(25)

# table generator
def print_table(n):
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')

print_table(6)

# reverse a string
def reverse_string(data):
    print(data[::-1])

reverse_string("Python")

# count vowels
def count_vowels(data):
    vowels = "aeiou"
    count = 0
    for i in data.lower():
        if i in vowels:
            count += 1
    print(f'Vowels count: {count}')

count_vowels("Hello World")

# simple calculator
def calculator(a, b, op):
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("Invalid operator")

calculator(10, 5, "*")
