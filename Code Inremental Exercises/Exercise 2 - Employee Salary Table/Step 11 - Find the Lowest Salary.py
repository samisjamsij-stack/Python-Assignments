# =====================================
# Step 11 - Find Lowest Salary
# =====================================

salaries = [
    [5000, 5200, 5100],
    [4800, 4950, 5050],
    [6000, 6100, 6200]
]

# 1. Assume the first salary is the lowest.
lowest = salaries[0][0]

# 2. Check every salary.
for row in salaries:

    for salary in row:

        # 3. Is this salary smaller?
        if salary < lowest:

            # 4. Save the new lowest salary.
            lowest = salary

# 5. Display the result.
print("Lowest Salary =", lowest)