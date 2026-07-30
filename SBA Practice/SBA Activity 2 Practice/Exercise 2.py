# Store the sales of three stores for four months.

sales_numbers = [
    [1200, 1500, 1800, 2000],
    [1400, 1600, 1900, 2200],
    [1300, 1700, 2100, 2300]
]

total = 0

for row in sales_numbers:
    for value in row:
        total += value
print("Total =", total)