# Program 10_Total

# Create a list.
numbers = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]

# Make a new variable to gather the total from the list.
total = 0

# Create a nested loop to gather the values from the list.
# Gather the total from the list, then print the total.
for row in numbers:
    for value in row:
        total += value
print("Total =", total)