# Task 2 - Multiply Two Numbers

# Exercise 1 
def multiply_numbers(a, b):
    return a * b

product = multiply_numbers(12,7)
print("Product = ", product)

# Exercise 2
def calculate_area(width, height):
    return width * height

width = float(input("Enter width:"))
height = float(input("Enter height: "))

area = calculate_area(width, height)
print("Area = ", area)

# Exercise 3
def calculate_volume(length, width, height):
    return length * width * height

length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
height = float(input("Enter Height: "))

volume = calculate_volume(length, width, height)
print("Volume = ", volume)