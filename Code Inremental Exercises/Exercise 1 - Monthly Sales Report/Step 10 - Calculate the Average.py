# ----------------------------------------
# Step 10 - Calculate Average
# ----------------------------------------

sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]

grand_total = 0
count = 0

# 1. Process every sales amount.
for row in sales:

    for amount in row:

        grand_total += amount
        count += 1

# 2. Calculate the average.
average = grand_total / count

# 3. Print the average.
print("Average = $", round(average, 2))