# Program 13_Student_Marks

# Create a list.
students = [
["Alice", 85, 90, 88],
["Bob", 75, 82, 91],
["Charlie", 95, 89, 94]
]

# Create a for loop to go through the array.
# The name variable gathers the student in position [0] on the list.
# The total variable gathers students in positions [1], [2], [3].
# The average takes the total and divides it by 3.
for student in students:
    name = student [0]
    total = student[1] + student[2] + student[3]
    average = total / 3

# Display the name, total, and average for each student.
    print(name)
    print("Total:", total)
    print("Average:", average)
    print()