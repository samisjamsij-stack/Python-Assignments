# Step 5 - Find Lowest Price

prices = [
    [12.99, 8.50, 15.75],
    [5.99, 9.49, 14.99],
    [20.00, 18.50, 7.25]
]

# Assume the first price is the lowest.
lowest = prices[0][0]

for row in prices:

    for price in row:

        print(f"${price:.2f}", end="\t")

        # Is this price smaller?
        if price < lowest:
            lowest = price

    print()

print("\nCheapest = $", lowest)