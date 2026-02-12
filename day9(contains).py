class Library:
    def __init__(self, book):
        self.book = book
    def __contains__(self, item):
        if item in self.book:
            print("It contain book")
        else:
            print("Not contains")

obj = Library(["oops","fullstack","The Story","The jungel book"])
obj.__contains__("oops")
