# Step 4 - Find Highest Price

prices = [
    [12.99, 8.50, 15.75],
    [5.99, 9.49, 14.99],
    [20.00, 18.50, 7.25]
]

# Assume the first price is the highest.
highest = prices[0][0]

for row in prices:

    for price in row:

        print(f"${price:.2f}", end="\t")

        # Is this price larger?
        if price > highest:
            highest = price

    print()

print("\nMost Expensive = $", highest)