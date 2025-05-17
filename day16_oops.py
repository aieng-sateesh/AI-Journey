# Day 16 – OOP Mini Project #2: Student Management System
# Author: Sateesh Kumar
# Date: 16/05/2025

# 🔸 Define the Student class
class Student:
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display_info(self):
        # Return student info as a formatted string
        return f'Name: {self.name}, Age: {self.age}, CGPA: {self.cgpa}'

    def update_cgpa(self, new_cgpa):
        # Update the student's CGPA
        self.cgpa = new_cgpa

# 🔹 Create student objects
student1 = Student('Ali', 12, 2.3)
student2 = Student('Usman', 23, 3.2)
student3 = Student('Naveed', 21, 3.1)

# 🔹 Store students in a list
all_students = [student1, student2, student3]

# 🔹 Display initial student info
print("📋 Student Info (Before CGPA Update):")
for student in all_students:
    print(student.display_info())

# 🔹 Update CGPA of student1
student1.update_cgpa(3.2)

# 🔹 Display updated info
print("\n🔁 Student Info (After CGPA Update):")
for student in all_students:
    print(student.display_info())
