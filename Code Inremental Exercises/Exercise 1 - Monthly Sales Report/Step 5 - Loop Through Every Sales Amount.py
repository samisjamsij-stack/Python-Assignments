# ----------------------------------------
# Step 5 - Nested Loops
# ----------------------------------------

sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]

# 1. Loop through every store.
for row in sales:

    # 2. Loop through every month's sales.
    for amount in row:

        # 3. Print one sales amount.
        print(amount)