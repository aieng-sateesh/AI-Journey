# Day 16 – OOP Mini Project #3: Bank Account with Error Handling and Inheritance

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f'Account created for {self.name} with balance {self.balance}.')

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit must be greater than 0.")
            self.balance += amount
            print(f'Deposited {amount}. New balance: {self.balance}')
        except ValueError as e:
            print("❌", e)

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')
        except ValueError as e:
            print("❌", e)

    def get_balance(self):
        print(f'Your current balance is {self.balance}')

# Child class inherits BankAccount
class SavingsAccount(BankAccount):
    def apply_interest(self):
        interest = self.balance * 0.1  # 10% interest
        self.balance += interest
        print(f' Interest of {interest} applied. New balance: {self.balance}')


# 🔽 Example usage
acc = BankAccount('Ali', 20000)
acc.deposit(3000)
acc.withdraw(25000)  # Will trigger error
acc.get_balance()

print("\n🔁 Using Savings Account with interest")
save_acc = SavingsAccount('Ali', 20000)
save_acc.apply_interest()
save_acc.get_balance()
