# Exercise 1 - Create a class called Laptop.
# Store: brand, price. 
# Print both.

class Laptop:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

laptop1 = Laptop("Dell", "$1,200")

print(laptop1.brand)
print(laptop1.price)

# Exercise 2 - Create a class called City.
# Store: city name, population
# Print both

class City:

    def __init__(self, city_name, population):
        self.name = city_name
        self.pop = population

city1 = City("Fresno", "555,500")

print(city1.name)
print(city1.pop)