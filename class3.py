## 3. BankAccount — Deposit Money

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. \nNew balance: {self.balance}")

acc = BankAccount(100)
acc.deposit(50)


