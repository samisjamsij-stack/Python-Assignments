# Problem: A company has 3 stores.
# Each store reports sales for 4 months.

# Store the sales in a 2D array.
sales = [
    [2500, 3000, 2800, 3500],
    [4000, 4200, 3900, 4100],
    [1800, 2100, 2400, 2600]
]

# Calculate the grand total.
grand_total = 0

for row in sales:

    for amount in row:

        grand_total += amount
        amount += 1

# 2. Calculate the average.
average = grand_total / amount
# Display all sales.
print("Average Monthly Sales: ", average)
print("Grand Total: ", grand_total)