# Exercise 1 - Create a class called Player.
# Store the player's name.
# Create an introduce() method that prints: "My name is ..."

class Player:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is ", self.name)

player1 = Player("James")

player1.introduce()

# Exercise 2 - Create a class called Pet
# Store the pet's name.
# Create a method that prints: "My pet is ..."

class Pet:

    def __init__(self, name):
        self.name = name

    def pet_name(self):
        print("My pet is Lucky", self.name)

pet1 = Pet("Lucky")
pet1.pet_name()