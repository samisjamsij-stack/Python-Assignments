# Step 7 - Total and Lowest

prices = [
    [12.99, 8.50, 15.75],
    [5.99, 9.49, 14.99],
    [20.00, 18.50, 7.25]
]

total = 0
lowest = prices[0][0]

for row in prices:

    for price in row:

        print(f"${price:.2f}", end="\t")

        total += price

        if price < lowest:
            lowest = price

    print()

print("\nTotal Value = $", round(total, 2))
print("Cheapest = $", lowest)