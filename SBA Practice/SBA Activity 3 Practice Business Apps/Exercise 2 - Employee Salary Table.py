# Problem: A company has three departments.
# Each row represents salaries of employees in one department.
# Find the highest salary.
# Find the lowest salary.

salaries = [
    [5000, 5200, 5100],
    [4800, 4950, 5050],
    [6000, 6100, 6200]
]

highest = salaries[0][0]
lowest = salaries [0][0]

for row in salaries:
    for salary in row:
        if salary > highest:
            highest = salary
else:
    lowest <= salaries[0][0]
    print("Lowest Salary = ", lowest)

print("Highest Salary = ", highest)