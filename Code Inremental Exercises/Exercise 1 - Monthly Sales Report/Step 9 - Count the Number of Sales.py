# ----------------------------------------
# Step 9 - Count Values
# ----------------------------------------

sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]

# 1. Create a counter.
count = 0

# 2. Loop through every value.
for row in sales:

    for amount in row:

        # 3. Increase the counter.
        count += 1

# 4. Print the number of values.
print("Count =", count)