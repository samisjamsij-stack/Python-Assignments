# ----------------------------------------
# Step 11 - Complete Monthly Sales Report
# ----------------------------------------

# 1. Create the 2D list.
sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]

# 2. Create variables.
grand_total = 0
count = 0

# 3. Print the heading.
print("Monthly Sales Report")

# 4. Process each store.
for row in sales:

    # 5. Process each month's sales.
    for amount in row:

        # 6. Display the sales amount.
        print(f"${amount}", end="\t")

        # 7. Add to the grand total.
        grand_total += amount

        # 8. Increase the counter.
        count += 1

    # 9. Move to the next line.
    print()

# 10. Calculate the average.
average = grand_total / count

# 11. Display the results.
print("\nGrand Total = $", grand_total)
print("Average Monthly Sales = $", round(average, 2))
