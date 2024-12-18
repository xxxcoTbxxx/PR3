class FinanceCalculator:
    def __init__(self):
        self.balance = 0

    def add_income(self, amount):
        self.balance += amount
        return self.balance

    def add_expense(self, amount):
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def add_tax(self, tax):
        self.balance -= tax
        return self.balance
