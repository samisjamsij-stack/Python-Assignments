# Step 1 - Display Product Prices

prices = [
    [12.99, 8.50, 15.75],
    [5.99, 9.49, 14.99],
    [20.00, 18.50, 7.25]
]

# Loop through each row.
for row in prices:

    # Loop through each price.
    for price in row:

        # Display the price.
        print(price, end="\t")

    # Move to the next line.
    print()