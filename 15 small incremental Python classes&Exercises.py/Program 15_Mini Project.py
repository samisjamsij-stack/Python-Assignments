# Exercise 1 - Create a class called Book.
# Store: title, author, pages
# Create a method called show().
# Display all books using a loop.

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Pages: ", self.pages)
        print()

book1 = Book("Green, Eggs, and Ham", "Dr. Seuss", 56 )
book2 = Book("To Kill a Mockingbirg", "Tom Saywer", 200)
book3 = Book("Judy B Jones", "Judy Jones", 90)

books = [book1, book2, book3]

for book in books: 
    book.show()

# Exercise 2 - Create a class called Car. 

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Year: ", self.year)

car1 = Car("Toyota", "Hybrid", 2008)
car2 = Car("Haundai", "Tuscon", 2015)
car3 = Car("Honda", "Hybrid", 2013)

cars = [car1, car2, car3]

for car in cars:
    car.show()
