## 4. BankAccount — Withdraw Money

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

acc = BankAccount(100)
acc.withdraw(30)
acc.withdraw(20)
acc.withdraw(60)
