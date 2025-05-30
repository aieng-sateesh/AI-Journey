# Day 20 - Billing System using OOP

# define item class
class Item:
    def __init__(self, name, price, quantity):  # constructor for item
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):  # calculate total price for item
        return self.price * self.quantity

# define bill manager class
class BillManager:
    def __init__(self):
        self.items = []  # store all added items

    def add_item(self, item):  # add item to bill
        self.items.append(item)

    def show_bill(self):  # print all items with total price
        print("Bill Summary:")
        for item in self.items:
            print(f'{item.name} × {item.quantity} = {item.get_total_price()} Rs')

    def calculate_total(self):  # calculate final bill amount
        total = sum(item.get_total_price() for item in self.items)
        print(f'Total Amount = {total} Rs')

# sample usage
i1 = Item("Milk", 60, 2)
i2 = Item("Chips", 30, 3)

bill = BillManager()
bill.add_item(i1)
bill.add_item(i2)
bill.show_bill()
bill.calculate_total()
