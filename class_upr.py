class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def price_with_vat(self):
        pwv = self.price * 1.2
        return f"£{pwv:.2f}"
    def describe(self):
        return f"{self.title} - £{self.price:.2f}"

book1 = Book("Book 1", 10)
book2 = Book("Book 2", 20)

print(book1.describe())
print(book2.price_with_vat())
print(book1.title)