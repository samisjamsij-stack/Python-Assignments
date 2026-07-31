# Step 2 - Format Prices

prices = [
    [12.99, 8.50, 15.75],
    [5.99, 9.49, 14.99],
    [20.00, 18.50, 7.25]
]

for row in prices:

    for price in row:

        # Display with two decimal places.
        print(f"${price:.2f}", end="\t")

    print()