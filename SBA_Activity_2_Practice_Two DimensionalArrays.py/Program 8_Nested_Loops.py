# Program 8_Nested_Loops

# Create a list.
numbers = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]

# Create a nest for loop to gather the numbers in the rows.
# After gathering the values in the rows print them.
for row in numbers:
    for value in row:
        print(value)