# Exercise 3 - Inventory Management (Final Solution)

# 1. Create a variable to store the total inventory.
total = 0

# 2. Create a variable to count products with more than 20 units.
count = 0

# 3. Create the inventory table.
inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

# 4. Loop through each warehouse row.
for row in inventory:

    # 5. Loop through each inventory quantity.
    for item in row:

        # 6. Display the inventory quantity.
        print(item, end="\t")

        # 7. Add the quantity to the total inventory.
        total += item

        # 8. Check if the quantity is greater than 20.
        if item > 20:

            # 9. Increase the counter.
            count += 1

    # 10. Move to the next row.
    print()

# 11. Display the total inventory.
print("\nTotal Inventory =", total)

# 12. Display the number of products with more than 20 units.
print("Products Above 20 Units =", count)