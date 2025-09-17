# Project 33: Bank Account Class
# Topic: OOP with deposit, withdraw, balance check

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}$ deposited. New balance: {self.balance}$")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount}$ withdrawn. New balance: {self.balance}$")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        print(f"Current balance: {self.balance}$")

account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.get_balance()
