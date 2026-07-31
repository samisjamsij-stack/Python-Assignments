# ----------------------------------------
# Step 6 - Print Like a Table
# ----------------------------------------

sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]

# 1. Loop through each store.
for row in sales:

    # 2. Loop through each sales amount.
    for amount in row:

        # 3. Print on the same line.
        print(amount, end="\t")

    # 4. Move to the next row.
    print()