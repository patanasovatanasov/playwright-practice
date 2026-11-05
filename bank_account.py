
class BankAccount:
    balance = 0
    def __init__(self):
        balance = self.balance

    def add_money(self, n):
        if n <= 0 :
            raise ValueError("Enter correct value!")
        else:
            self.balance += n

    def withdraw_money(self, w):
        if w > self.balance:
            raise ValueError("Insufficient amount!")
        else:
            self.balance -= w
