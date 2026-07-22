# Task 1 Example
# def add_numbers(num1, num2):
#   return num1 + num2
#   answer = add_numbers(15, 25)
#   print("Answer:", answer)

# Task 1 - Add Two Numbers - Exercise 1
# Create a function named add_numbers() that returns the
# sum of 18 and 42.

def add_numbers(num1, num2):
    return num1 + num2
answer = add_numbers(18,42)
print("Answer =", answer)

# Exercise 2 - Ask the user for two numbers and return the total.

def add_numbers(num1, num2):
    return num1 + num2

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

total = add_numbers(first, second)
print("The total is:", total)

# Exercise 3 - Add three numbers.

def add_three_numbers(num1, num2, num3):
    return num1 + num2 + num3

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))

total = add_three_numbers(number1, number2, number3)
print("Total =", total)