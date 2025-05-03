# Day 4 - Student CGPA Calculator using Dictionaries and Loops
# Author: Sateesh Kumar
# Date: 04/05/2025

# Create an empty list to store student dictionaries
students = []

# Input student details using a loop
for i in range(1, 4):
    print(f"\nEnter details for Student {i}:")
    name = input(f"Enter student {i} name: ")
    age = int(input(f"Enter student {i} age: "))
    cgpa = float(input(f"Enter student {i} CGPA: "))

    # Create a dictionary for each student
    student = {
        "name": name,
        "age": age,
        "cgpa": cgpa
    }

    # Add student dictionary to the list
    students.append(student)

# Print all student details
print("\n📋 All Student Details:")
for student in students:
    print(student)

# Calculate average CGPA using a for loop
total_cgpa = 0
for student in students:
    total_cgpa += student["cgpa"]

average_cgpa = total_cgpa / len(students)
print(f"\n🎯 Average CGPA of all students is: {round(average_cgpa, 2)}")
