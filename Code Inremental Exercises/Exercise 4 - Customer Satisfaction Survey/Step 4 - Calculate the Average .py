# Step 4 - Calculate Average Rating

ratings = [
    [5, 4, 5],
    [3, 5, 4],
    [5, 5, 5]
]

total = 0
count = 0

for row in ratings:

    for rating in row:

        print(rating, end=" ")

        total += rating
        count += 1

    print()

# Calculate average.
average = total / count

print("\nAverage Rating =", average)