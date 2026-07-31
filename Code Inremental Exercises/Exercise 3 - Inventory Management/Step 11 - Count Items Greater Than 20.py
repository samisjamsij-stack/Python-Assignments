# Step 11 - Count Products Above 20

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

count = 0

for row in inventory:

    for item in row:

        if item > 20:

            count += 1

print("Products Above 20 Units =", count)