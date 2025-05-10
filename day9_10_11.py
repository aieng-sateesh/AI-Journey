# Day 9, 10 & 11 - Tuples, Sets, File I/O, zip(), enumerate()
# Author: Sateesh Kumar
# Date: 09/05/2025 to 11/05/2025

# ----------------------
# 📘 Day 9: Tuples and Sets
# ----------------------

# 🔷 Tuple Example (Immutable, Ordered)
my_tuple = ("Python", "AI", 2025)
print("Tuple Element:", my_tuple[0])
print("Tuple Length:", len(my_tuple))

# Tuple unpacking
lang, field, year = my_tuple
print(f"{lang} is used in {field} in {year}")

# 🔶 Set Example (Unordered, No Duplicates)
my_set = {1, 2, 2, 3, 4}
print("Set (duplicates removed):", my_set)

my_set.add(5)
my_set.remove(3)
if 2 in my_set:
    print("2 is in the set")

# ----------------------
# 📁 Day 10: File Handling
# ----------------------

# Create and write to a file
with open("notes.txt", "w") as file:
    file.write("Python is a powerful language for AI and data science.\n")

# Read the file
with open("notes.txt", "r") as file:
    content = file.read()
    print("\nContent from file:\n", content)

# Append to the file
with open("notes.txt", "a") as file:
    file.write("It supports file handling very well.\n")

# Count total words in the file
with open("notes.txt", "r") as file:
    words = file.read().split()
    print("Total words:", len(words))

# Read line by line with line numbers
with open("notes.txt", "r") as file:
    for idx, line in enumerate(file, start=1):
        print(f"Line {idx}: {line.strip()}")

# ----------------------
# 🔁 Day 11: zip() and enumerate() Practice
# ----------------------

# Using zip() to combine two related lists
names = ["Ali", "Sara", "Usman"]
marks = [88, 92, 79]

print("\nStudent Marks:")
for name, mark in zip(names, marks):
    print(f"{name} scored {mark}")

# Using enumerate() to get index and value
tools = ["Python", "Numpy", "Pandas"]

print("\nTools with Index:")
for index, tool in enumerate(tools):
    print(f"{index + 1}. {tool}")

# zip() + enumerate() together to rank students
print("\nStudents with Ranking:")
for rank, (name, mark) in enumerate(zip(names, marks), start=1):
    print(f"{rank}) {name} → {mark} marks")
