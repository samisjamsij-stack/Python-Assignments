# Step 8 - Calculate Total Inventory

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

total = 0

for row in inventory:

    for item in row:

        total += item

print("Total Inventory =", total)