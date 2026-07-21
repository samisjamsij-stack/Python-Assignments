# Exercise 1 - Create a Book. 
# Change the title after creating the object.
# Print the new title.

class Book:
    def __init__(self, name):
        self.name = name

book1 = Book("To kill a Mockingbird")

book1.name = "Fahrenheit 541"

print(book1.name)

# Exercise 2 - Create a Phone. 
# Change the model.
# Print the updated title.

class Phone:
    def __init__(self, name):
        self.name = name

phone1 = Phone("Samsung")

phone1.name = "iPhone"

print(phone1.name)