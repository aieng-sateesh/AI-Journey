# Day 7 - String Handling in Python
# Author: Sateesh Kumar
# Date: 07/05/2025

# Part 1: Slicing Strings
name = 'Sateesh kumar'
print("Length:", len(name))
print("Slice [2:5]:", name[2:5])
print("Slice [-5:-1]:", name[-5:-1])
print("Slice [2:8:2]:", name[2:8:2])

# Part 2: String Functions
first_name = 'sateesh'
second_name = 'KUMAR'
print("Upper:", first_name.upper())
print("Lower:", first_name.lower())
print("Title:", first_name.title())
print("Count of 'e':", first_name.count('e'))
print("Replace:", first_name.replace('sateesh','mustafa'))
print("Find 't':", first_name.find('t'))
print("Join:", first_name.join(second_name))

# Part 3: Password Strength Checker
password = input("Enter your password: ")
if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Strong password 💪")
else:
    print("Weak password. Try including uppercase letters, digits, and make it at least 8 characters.")
