# Day 6 - Python Loops and Patterns
# Author: Sateesh Kumar
# Date: 06/05/2025

# 1. Print numbers from 1 to 10 using for loop
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 1 to 20 using while loop
init = 1
final = 20
print('Even numbers from 1 to 20:')
while init <= final:
    if init % 2 == 0:
        print(init)
    init += 1

# 3. Print table of 5
for i in range(1, 11):
    print(f'Table of 5 is 5 * {i} = {5 * i}')

# 4. Decreasing Number Pattern with variable step (k)
k = 2
for i in range(12, 22):
    print(i - k)
    k += 2

# 5. Continue statement demo
for i in range(1, 11):
    if i == 4:
        continue
    print(i)

# 6. Break statement demo
for i in range(1, 11):
    print(i)
    if i == 4:
        break

# 7. Simple increasing star pattern
for i in range(1, 5):
    print(i * '*')
