# Step 9 - Display and Add

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

total = 0

for row in inventory:

    for item in row:

        print(item, end="\t")
        total += item

    print()

print("\nTotal Inventory =", total)