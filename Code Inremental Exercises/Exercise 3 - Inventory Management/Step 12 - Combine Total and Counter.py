# Step 12 - Total and Counter Together

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

total = 0
count = 0

for row in inventory:

    for item in row:

        total += item

        if item > 20:
            count += 1

print("Total Inventory =", total)
print("Products Above 20 Units =", count)