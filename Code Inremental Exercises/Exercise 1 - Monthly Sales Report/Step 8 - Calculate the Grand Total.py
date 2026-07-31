# ----------------------------------------
# Step 8 - Grand Total
# ----------------------------------------

sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]

# 1. Create a variable to store the total.
grand_total = 0

# 2. Loop through every sales amount.
for row in sales:

    for amount in row:

        # 3. Add each value to the total.
        grand_total += amount

# 4. Display the total.
print("Grand Total = $", grand_total)