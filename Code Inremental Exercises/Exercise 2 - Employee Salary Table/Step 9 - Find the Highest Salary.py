# =====================================
# Step 9 - Find Highest Salary
# =====================================

salaries = [
    [5000, 5200, 5100],
    [4800, 4950, 5050],
    [6000, 6100, 6200]
]

# 1. Assume the first salary is the highest.
highest = salaries[0][0]

# 2. Check every salary.
for row in salaries:

    for salary in row:

        # 3. Is this salary larger?
        if salary > highest:

            # 4. Save the new highest salary.
            highest = salary

# 5. Display the result.
print("Highest Salary =", highest)