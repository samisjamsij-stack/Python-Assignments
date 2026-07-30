# Problem: A warehouse stores inventory quantities.
# Display the inventory.
# Calculate the total inventory.
# Count how many products have more than 20 units.

inventory = [
    [15, 20, 10],
    [8, 25, 30],
    [40, 35, 18]
]

total_inventory = 0
count = 0

for row in inventory:
    for amount in row:
        total_inventory += amount
        if amount >= 20:
                count += 1



print("Total inventory = ", total_inventory)
print("Units over 20 = ", count)