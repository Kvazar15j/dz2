class BankAccount:
    account_number = ""
    balance = 0

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, a):
        if a > 0:
            self.balance += a
            print(f"+{a} денег")
        else:
            print("не коректные данные")

    def withdraw(self, a):
        if self.balance >= a:
            self.balance -= a
            print(f"-{a} денег")
        else:
            print("Не достаточно средств")


