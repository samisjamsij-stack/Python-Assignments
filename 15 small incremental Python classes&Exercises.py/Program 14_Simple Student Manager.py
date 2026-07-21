# Exercise 1 - Create an Employee class.
# Add five employees to a list.
# Display every employee.

class Employee:
    def __init__(self, name):
        self.name = name

employees = []

employees.append(Employee("Mike"))
employees.append(Employee("Carry"))
employees.append(Employee("Penelope"))

for employee in employees:
    print(employee.name)

# Exercise 2 - Create Movie class.
# Store four movies inside a list.
# Print every movie title.

class Movie:
    def __init__(self, list):
        self.list = list

movies = []

movies.append(Movie("The Beekeeper"))
movies.append(Movie("The Menu"))
movies.append(Movie("Friday"))

for movie in movies:
    print(movie.list)