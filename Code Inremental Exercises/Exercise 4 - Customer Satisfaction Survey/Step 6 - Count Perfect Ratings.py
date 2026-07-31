# Step 6 - Count Perfect Ratings

ratings = [
    [5, 4, 5],
    [3, 5, 4],
    [5, 5, 5]
]

total = 0
count = 0

# Count perfect ratings.
perfect = 0

for row in ratings:

    for rating in row:

        print(rating, end=" ")

        total += rating
        count += 1

        # Check for a perfect rating.
        if rating == 5:

            perfect += 1

    print()

average = total / count

print("\nAverage Rating =", round(average, 2))
print("Perfect Ratings =", perfect)