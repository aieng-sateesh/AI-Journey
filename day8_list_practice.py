# Day 8 - Python List Practice
# Author: Sateesh Kumar
# Date: 08/05/2025

# 1. Add 5 numbers from user and print average
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

average = sum(numbers) / len(numbers)
print(f"\nAverage of the numbers is: {round(average, 2)}")

# 2. Work with list of 10 numbers
num_list = [2, 5, 8, 11, 4, 9, 6, 13, 3, 10]

print("\nEven numbers:")
for n in num_list:
    if n % 2 == 0:
        print(n, end=' ')

print("\nOdd numbers:")
for n in num_list:
    if n % 2 != 0:
        print(n, end=' ')

print(f"\nTotal sum of list: {sum(num_list)}")

# 3. Sort list in ascending and descending order
data = [12, 4, 9, 1, 33, 8]
data.sort()
print(f"\nAscending order: {data}")
data.sort(reverse=True)
print(f"Descending order: {data}")

# 4. Remove duplicates from a list
dup_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_list = list(set(dup_list))
print(f"\nOriginal list with duplicates: {dup_list}")
print(f"List without duplicates: {unique_list}")
