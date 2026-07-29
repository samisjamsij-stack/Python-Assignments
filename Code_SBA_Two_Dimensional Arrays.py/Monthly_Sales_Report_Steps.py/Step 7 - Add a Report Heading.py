# ----------------------------------------
# Step 7 - Report Heading
# ----------------------------------------

sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]

# 1. Print the report title.
print("Monthly Sales Report")

# 2. Print every store.
for row in sales:

    for amount in row:
        print(f"${amount}", end="\t")

    print()
