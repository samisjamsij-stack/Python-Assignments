# Exercise 1 - Create five Car objects
# Store them in a list
# Print every brand.

class Car:

    def __init__(self, name):
        self.name = name

car1 = Car("Toyota")
car2 = Car("Hondai")
car3 = Car("Tesla")

cars = [car1,car2,car3]

for car in cars:
    print(car.name)

# Exercise 2 - Create four Fruit objects.
# Store them in a list.
# Print every fruit name.

class Fruit:
    def __init__(self, name):
        self.name = name

fruit1 = Fruit("Apple")
fruit2 = Fruit("Mango")
fruit3 = Fruit("Papaya")

fruits = [fruit1, fruit2, fruit3]

for fruit in fruits:
    print(fruit.name)