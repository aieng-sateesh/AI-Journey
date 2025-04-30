# Day 2 - Python Operators Project: Simple Calculator
# Author: Sateesh Kumar
# Description:
#   A menu-driven calculator that performs basic arithmetic operations.
#   Demonstrates Python operators, if-elif-else logic, user input, and loops.

# Display the menu options to the user
print('''
Welcome to Python Calculator 🧮
Choose an operation:
1: Addition
2: Subtraction
3: Multiplication
4: Division
5: Floor Division
6: Exponentiation
7: Modulus
''')

# Start an infinite loop so user can keep using the calculator
while True:
    # Take input from the user for two numbers
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    # Ask user to select an operation
    operation = int(input('Choose operation (1 to 7): '))

    # Perform the selected operation using if-elif-else
    if operation == 1:
        print(f"The Addition of {num1} and {num2} is {num1 + num2}")
    elif operation == 2:
        print(f"The Subtraction of {num1} and {num2} is {num1 - num2}")
    elif operation == 3:
        print(f"The Multiplication of {num1} and {num2} is {num1 * num2}")
    elif operation == 4:
        # Check for division by zero
        if num2 != 0:
            print(f"The Division of {num1} and {num2} is {num1 / num2}")
        else:
            print("❌ Cannot divide by zero.")
    elif operation == 5:
        if num2 != 0:
            print(f"The Floor Division of {num1} and {num2} is {num1 // num2}")
        else:
            print("❌ Cannot floor divide by zero.")
    elif operation == 6:
        print(f"{num1} raised to the power of {num2} is {num1 ** num2}")
    elif operation == 7:
        if num2 != 0:
            print(f"The Modulus of {num1} and {num2} is {num1 % num2}")
        else:
            print("❌ Cannot perform modulus with zero.")
    else:
        print("⚠️ Invalid operation choice. Please select 1 to 7.")

    # Ask user if they want to perform another operation
    ask_again = input("Do you want to continue? (Y/N): ").strip().lower()

    # Continue or break based on user input
    if ask_again == 'y':
        continue
    elif ask_again == 'n':
        print("👋 Thank you for using the calculator!")
        break
    else:
        print("⚠️ Invalid input. Exiting.")
        break
