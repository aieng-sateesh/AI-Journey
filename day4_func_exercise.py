# Day 4 - Python Function Practice Exercises
# Author: Sateesh Kumar
# Date: 04/05/2025

# 🔢 Function to check if a number is even or not
def is_even(n):
    if n % 2 == 0:
        print(f"✅ Given number {n} is even.")
    else:
        print(f"❌ Given number {n} is not even.")

# Call the function
is_even(555)


# 🌡️ Function to convert Celsius to Fahrenheit
def convert_c_to_f(celsius):
    fahrenheit = ((9 / 5) * celsius) + 32
    print(f"🌡️ {celsius}°C is equal to {fahrenheit}°F.")

# Call the function
convert_c_to_f(39)


# 🙋‍♂️ Function to get user details (name and CGPA)
def details():
    name = input("Enter your name: ")
    cgpa = float(input("Enter your CGPA: "))
    print(f"Hello {name}, your CGPA is {cgpa}. Keep going strong!")

# Call the function
# details()  # Uncomment this if you're running interactively


# 📊 Function to calculate percentage
def calculate_percentage(marks_obtained, total_marks):
    percentage = (marks_obtained / total_marks) * 100
    print(f"📈 Your percentage is {round(percentage, 2)}%.")

# Call the function
calculate_percentage(412, 500)


# 🔍 Q8: Function to find the maximum number in a list
def find_max(numbers):
    print(f"🚀 The maximum number in the list is: {max(numbers)}")

# Call the function
find_max([56, 42, 54, 767, 789, 454, 535])
