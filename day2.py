class Book:
    def __init__(self, title, auther):
        self.title = title
        self.auther = auther
    def display_book(self):
        print("The title of the book is", self.title, "auther of this book", self.auther)

class Issuebook(Book):
    def __init__(self, title, auther, issued_to, issued_date):
        self.issued_to = issued_to
        self.issued_date = issued_date
        super().__init__(title, auther)

    def display_issue_book(self):
        print("the details of book and book issued", self.title, self.auther, self.issued_to, self.issued_date)

issued_book  = Issuebook("Happy day", "bosco", "vinay", "12-1-2026" )      
issued_book.display_book()
issued_book.display_issue_book()