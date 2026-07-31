# Step 6 - Display Items Like a Table

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

for row in inventory:

    for item in row:
        print(item, end="\t")

    print()