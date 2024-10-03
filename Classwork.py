class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else: self.balance -= amount
account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
print(account.balance)