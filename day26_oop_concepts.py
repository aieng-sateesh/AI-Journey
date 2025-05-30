# Day 26 - OOP Concept Practice (Classmethod, Staticmethod, Object Count)

# Laptop class to track total laptops
class Laptop:
    total_laptops = 0

    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
        Laptop.total_laptops += 1

    def show_details(self):
        print(f'Laptop | Brand: {self.brand} | RAM: {self.ram}GB | Price: {self.price}')

    def apply_discount(self, percent):
        discount = self.price * percent
        print(f'Price after {int(percent * 100)}% discount: {self.price - discount}')

    def show_total_laptops(self):
        print(f'Total laptops sold: {Laptop.total_laptops}')


# MobileStore class to track total mobiles
class MobileStore:
    total_mobiles = 0

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        MobileStore.total_mobiles += 1

    def show_details(self):
        print(f'Mobile | Brand: {self.brand} | Price: {self.price}')

    @classmethod
    def total_mobile(cls):
        print(f'Total mobiles sold: {cls.total_mobiles}')

    @staticmethod
    def mobile_pros():
        print('Mobiles are essential for communication and productivity.')

# sample usage for Laptop
l1 = Laptop("Dell", 8, 56000)
l2 = Laptop("HP", 16, 78000)
l1.show_details()
l2.apply_discount(0.1)
l2.show_total_laptops()

# sample usage for MobileStore
m1 = MobileStore("Samsung", 45000)
m2 = MobileStore("Apple", 100000)
m3 = MobileStore("Redmi", 25000)
m1.show_details()
m2.show_details()
m3.show_details()
MobileStore.total_mobile()
MobileStore.mobile_pros()
