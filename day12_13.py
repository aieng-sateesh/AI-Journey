# Day 12 & 13 – Advanced Python Practice: OOP, Lambda, NumPy, Pandas
# Author: Sateesh Kumar
# Date: 13/05/2025

# 🔹 OOP: Vehicle and Car with inheritance

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def info(self):
        print(f"Vehicle Name: {self.name}, Speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type

    def info(self):
        print(f"Car Name: {self.name}, Speed: {self.speed} km/h, Fuel: {self.fuel_type}")

# Create objects
v1 = Vehicle("Civic", 210)
v1.info()

c1 = Car("Civic", 210, "Diesel")
c1.info()


# 🔹 Lambda Function with map() and filter()

nums = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x * x, nums))
print("\nSquares using lambda:", squares)

nums2 = [34, 2, 21, 4, 76, 7, 12, 1, 34]
greater_than_10 = list(filter(lambda x: x > 10, nums2))
print("Filtered (>10):", greater_than_10)


# 🔹 NumPy Practice: Stats on random numbers

import numpy as np
import random

random_nums = [random.randint(1, 100) for _ in range(10)]
arr = np.array(random_nums)

print("\nNumPy Array:", arr)
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Sorted:", np.sort(arr))


# 🔹 Pandas Practice: DataFrame with Result Column

import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Usman", "Ayesha", "Bilal"],
    "Age": [18, 19, 17, 18, 20],
    "Marks": [56, 32, 71, 39, 85]
}

df = pd.DataFrame(data)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x > 40 else "Fail")

print("\nStudent DataFrame:")
print(df)

print("\nStudents Who Passed:")
print(df[df["Result"] == "Pass"])
