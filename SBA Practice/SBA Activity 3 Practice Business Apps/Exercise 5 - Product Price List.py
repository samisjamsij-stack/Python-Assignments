# Problem: A company sells products in three categories.
# Display all prices.
# Find the most expensive product
# Find the cheapest product.
# Calculate the total value of all listed products.

products = [
    [12.50, 18.75, 20.00],
    [30.00, 25.50, 40.25],
    [8.99, 10.99, 14.99]
]

total = 0
expensive = products[0][0]
cheapest = products[0][0]

for row in products:
    for product in row:
        if product > expensive:
            expensive = product
else:
    cheapest <= products[0][0]
    print("Cheapest = ", cheapest)
    print("Most Expensive = ", expensive)

for row in products:
    for amount in row:
        total += amount
        amount += 1

print("Total sales: ", total)