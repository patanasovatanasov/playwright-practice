class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add(self, name, price):
        self.cart[name] = price

    def remove(self, name):
        self.cart.pop(name)

    def total(self):
        return sum(self.cart.values())