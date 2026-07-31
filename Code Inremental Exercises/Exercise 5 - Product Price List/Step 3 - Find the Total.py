# Step 3 - Find Total Value

prices = [
    [12.99, 8.50, 15.75],
    [5.99, 9.49, 14.99],
    [20.00, 18.50, 7.25]
]

# Store the total.
total = 0

for row in prices:

    for price in row:

        print(f"${price:.2f}", end="\t")

        # Add the current price.
        total += price

    print()

print("\nTotal Value = $", round(total, 2))