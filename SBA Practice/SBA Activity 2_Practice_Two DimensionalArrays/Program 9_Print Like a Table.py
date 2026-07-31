# Program 9_Table_Format

numbers = [
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
]

# Create a nested for loop. Gather the values in the row.
# Create a table with the printed values.
for row in numbers:
    for value in row:
        print(value, end="\t")
print()