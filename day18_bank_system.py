# Day 18 - Bank System using OOP

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'New balance after deposit is {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'New balance after withdrawal is {self.balance}')
        else:
            print('Insufficient balance')

    def get_balance(self):
        print(f'Current balance is {self.balance}')

class SavingsAccount(BankAccount):
    def apply_interest(self):
        interest = self.balance * 0.1
        self.balance += interest
        print(f'Interest applied: {interest}, new balance is {self.balance}')

# Usage
acc1 = BankAccount("Ali", 20000)
acc1.deposit(3000)
acc1.withdraw(5000)
acc1.get_balance()

acc2 = SavingsAccount("Usman", 15000)
acc2.apply_interest()
acc2.get_balance()
