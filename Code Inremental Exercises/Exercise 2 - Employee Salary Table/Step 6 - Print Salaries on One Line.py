# =====================================
# Step 6 - Print on One Line
# =====================================

salaries = [
    [5000, 5200, 5100],
    [4800, 4950, 5050],
    [6000, 6100, 6200]
]

# 1. Loop through each department.
for row in salaries:

    # 2. Loop through each salary.
    for salary in row:

        # 3. Display each salary on the same line.
        print(salary, end="\t")

    # 4. Move to the next row.
    print()