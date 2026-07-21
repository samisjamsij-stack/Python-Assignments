# Exercise 1 - Create four Robot object. 
# Each robot should have a greet() method.
# Use a loop to a call every greeting.

class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

robots = [
    Robot("I'm Telsa, hello."),
    Robot("I'm Bob, Hello World."),
    Robot("I am Optimus Prime.")
]

for robot in robots:
    robot.greet()

# Exercise 2 - Create four Student object. 
# Each robot should have a introduce() method.
# Use a loop to a call every greeting.

class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello", self.name)

students = [
    Student("My name is Mary"),
    Student("My name is Sue"),
    Student("My name is John")
]

for student in students:
    student.introduce()