# ✅ Part 1: Python Coding Questions

# 🔹 Beginner-Level:

# Q1: Check whether a number is even or odd.
num = int(input('Enter a number: '))  # Take input from the user
if num % 2 == 0:  # Check if the number is divisible by 2
    print(f"It's an even number {num}.")  # Print if it's even
else:
    print(f"It's an odd number {num}.")  # Print if it's odd

# Q2: Function to convert Celsius to Fahrenheit.
def C_to_F():
    celsius_temp = float(input('Enter the temperature in Celsius: '))  # Input temperature in Celsius
    convert_to_f = celsius_temp * 9 / 5 + 32  # Convert to Fahrenheit
    print(f'Converted temperature in Fahrenheit is {convert_to_f}.')  # Print the converted temperature

C_to_F()  # Call the function

# Q3: Build a basic CGPA calculator using input from 3 subjects.
physics = float(input('Enter physics marks: '))  # Input physics marks
chemistry = float(input('Enter chemistry marks: '))  # Input chemistry marks
math = float(input('Enter math marks: '))  # Input math marks

total_marks = 300  # Total marks for 3 subjects
marks_obtained = physics + chemistry + math  # Calculate total marks obtained

cgpa = marks_obtained / total_marks * 100  # Calculate CGPA
print(f'CGPA is {round(cgpa, 2)}.')  # Print the CGPA rounded to 2 decimal places

# Q4: Function that reverses a string using slicing.
data = 'He is a good boy'  # Original string
print(data[::-1])  # Print the reversed string

# Q5: Create a multiplication table of a number using a for loop.
for i in range(1, 11):  # Loop from 1 to 10
    print(f'Table of 5 using for loop is 5 * {i} = {5 * i}.')  # Print multiplication table of 5

# 🔹 Intermediate-Level:

# Q1: Count vowels in a string.
data = 'Hi buddy, how are you'  # Input string
vowels_count = []  # List to store counts of vowels
for i in data:  # Loop through each character in the string
    if i in 'aeiou':  # Check if the character is a vowel
        vowels_count.append(1)  # Append 1 for each vowel
print(vowels_count.count(1))  # Print the total count of vowels

# Q2: Use a while loop to print all odd numbers from 1 to 50.
initial_num = 1  # Starting number
final_num = 50  # Ending number
odd_num = []  # List to store odd numbers
while initial_num <= final_num:  # Loop until the final number
    if initial_num % 2 != 0:  # Check if the number is odd
        odd_num.append(initial_num)  # Append odd number to the list
    initial_num += 1  # Increment the number
print(f'Odd numbers between 1 to 50 are {odd_num}.')  # Print the list of odd numbers

# Q3: Create a dictionary for 3 students and calculate the average CGPA.
student1 = {'name': 'Ali', 'age': 20, 'cgpa': 3.2}  # Student 1 data
student2 = {'name': 'Usman', 'age': 23, 'cgpa': 3.1}  # Student 2 data
student3 = {'name': 'Anwar', 'age': 33, 'cgpa': 3.8}  # Student 3 data

# Calculate average CGPA
average_cgpa = (student1.get('cgpa') + student2.get('cgpa') + student3.get('cgpa')) / 3
print(f'The average CGPA of 3 students is {round(average_cgpa, 2)}')  # Print average CGPA

# Q4: Function to check if a number is prime.
def is_prime(n):
    if n <= 1:  # Check if number is less than or equal to 1
        return False  # Not prime
    for i in range(2, n):  # Check divisibility from 2 to n-1
        if n % i == 0:  # If divisible, not prime
            return False
    return True 

#Q5
num=[1,2,3,4,5,6]
squared_num=list(map(lambda x:x*x,num))
print(squared_num)


# 🔹 Advanced Level Coding Questions

# Q1: Create a class Vehicle and subclass Car, overriding the info() method.
class Vehicle:
    def __init__(self, name, speed):
        self.name = name  # Initialize vehicle name
        self.speed = speed  # Initialize vehicle speed

    def info(self):
        # Print vehicle information
        print(f"Vehicle Name: {self.name}, Speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)  # Call the parent class constructor
        self.fuel_type = fuel_type  # Initialize fuel type

    def info(self):
        # Print car information, including fuel type
        print(f"Car Name: {self.name}, Speed: {self.speed} km/h, Fuel: {self.fuel_type}")

# Create objects of Vehicle and Car
v1 = Vehicle("Civic", 210)  # Create a Vehicle object
v1.info()  # Display vehicle info

c1 = Car("Civic", 210, "Diesel")  # Create a Car object
c1.info()  # Display car info

# Q2: Use NumPy to generate 10 random numbers and perform statistical operations.
import numpy as np
import random

# Generate a list of 10 random integers between 1 and 100
random_nums = [random.randint(1, 100) for _ in range(10)]
arr = np.array(random_nums)  # Convert the list to a NumPy array

# Print the NumPy array and perform statistical operations
print("\nNumPy Array:", arr)
print("Mean:", np.mean(arr))  # Calculate and print the mean
print("Max:", np.max(arr))  # Calculate and print the maximum value
print("Min:", np.min(arr))  # Calculate and print the minimum value
print("Sorted:", np.sort(arr))  # Print the sorted array

# Q3: Create a Pandas DataFrame with student data and add a Result column.
import pandas as pd

# Create a dictionary with student data
data = {
    "Name": ["Ali", "Sara", "Usman", "Ayesha", "Bilal"],
    "Age": [18, 19, 17, 18, 20],
    "Marks": [56, 32, 71, 39, 85]
}

df = pd.DataFrame(data)  # Create a DataFrame from the dictionary
# Add a Result column based on Marks
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x > 40 else "Fail")

# Print the DataFrame
print("\nStudent DataFrame:")
print(df)

# Print students who passed
print("\nStudents Who Passed:")
print(df[df["Result"] == "Pass"])

# Q4: Create a simple calculator using a menu-driven approach.
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

# Start an infinite loop so the user can keep using the calculator
while True:
    # Take input from the user for two numbers
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    # Ask user to select an operation
    operation = int(input('Choose operation (1 to 7): '))

    # Perform the selected operation using if-elif-else
    try: #ue try and except to avoid erros.
        if operation == 1:
            print(f"The Addition of {num1} and {num2} is {num1 + num2}")
        elif operation == 2:
            print(f"The Subtraction of {num1} and {num2} is {num1 - num2}")
        elif operation == 3:
            print(f"The Multiplication of {num1} and {num2} is {num1 * num2}")
        elif operation == 4:
            print(f"The Division of {num1} and {num2} is {num1 / num2}")
        elif operation == 5:
            print(f"The Floor Division of {num1} and {num2} is {num1 // num2}")
        elif operation == 6:
            print(f"{num1} raised to the power of {num2} is {num1 ** num2}")
        elif operation == 7:
            print(f"The Modulus of {num1} and {num2} is {num1 % num}")
        else:
            print("⚠️ Invalid operation choice. Please select 1 to 7.")
    except ZeroDivisionError:
        print("can't divide with zero.")
    except SyntaxError:
        print('syntax is not right.')

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
