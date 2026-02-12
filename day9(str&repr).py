class Book:
    def __init__(self, title, auther, price):
        self.title = title
        self.auther = auther
        self.price = price
    def __str__(self):
        return f"The title of the book is {self.title} auther is {self.auther} and the price of this books is {self.price}"
    def __repr__(self):
        return f"Title:{self.title}, Auther:{self.auther}, Price:{self.price}"

obj = Book("The story","Tommy",9000)
print(obj.__str__())
print(obj.__repr__())