# Task 3 - Find the Area of a Rectangle

# Exercise 1
def rectangle_area(length, width):
    return length * width

area = rectangle_area(9,6)
print("Area =", area)

# Exercise 2
def dimensions(length, width):
    return length * width

length = float(input("Enter length "))
width = float(input("Enter width "))

area = dimensions(length, width)
print("The rectangle area is ", area ,"square units")

# Exercise 3 - Calculate the total area of three different rectangles.
def rectangle_area(length, width):
    return length * width

total_area = 0

for rectangle in range(1,4):
    print("Rectangle", rectangle)

    length = float(input("Lenght "))
    width = float(input("Width "))

    area = rectangle_area(length, width)
    print("Area = ", area)
    total_area += area

print("/n Total Area = ", total_area)