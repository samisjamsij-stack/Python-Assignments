# Step 6 - Total and Highest

prices = [
    [12.99, 8.50, 15.75],
    [5.99, 9.49, 14.99],
    [20.00, 18.50, 7.25]
]

total = 0
highest = prices[0][0]

for row in prices:

    for price in row:

        print(f"${price:.2f}", end="\t")

        total += price

        if price > highest:
            highest = price

    print()

print("\nTotal Value = $", round(total, 2))
print("Most Expensive = $", highest)