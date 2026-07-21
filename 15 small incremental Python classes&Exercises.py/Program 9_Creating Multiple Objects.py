# Exercise 1 - Create three Book object. Print every book title.

class Book:
    def __init__(self, name):
        self.name = name

book1 = Book("Paramore")
book2 = Book("Brave New World")
book3 = Book("Tom Thumb")

print(book1.name)
print(book2.name)
print(book3.name)

# Exercise 2 - Create four Teacher objects. Print every Teacher's name

class Teacher:
    def __init__(self, name):
        self.name = name

teacher1 = Teacher("Ms. Mary")
teacher2 = Teacher("Ms. Dressel")
teacher3 = Teacher("Mrs. Joiner")

print(teacher1.name)
print(teacher2.name)
print(teacher3.name)