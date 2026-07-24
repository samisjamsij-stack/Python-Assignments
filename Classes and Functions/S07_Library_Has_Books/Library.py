from Books import Books

class Library:

    def __init__ (self):
        self.books = Books()

    def borrow_book(self):
        self.books.read()