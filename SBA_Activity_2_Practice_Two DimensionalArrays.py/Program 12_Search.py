# Program 12_Search

# Create a list.

numbers = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]

# Create a variable for both the target and the True/False statement.
target = 50

found = False

# Build a nested loop to go through each value in the list.
for row in numbers:
    for value in row:
        # The if statement is to determine if the values pulled from the list
        # are equal to the target variables.
        if value == target:
            found = True

# If the value holds true to equals the target, print "Found". Else, print "Not Found".
if found:
    print("Found")
else:
    print("Not Found")