# Step 3 - Count Ratings

ratings = [
    [5, 4, 5],
    [3, 5, 4],
    [5, 5, 5]
]

# Store total.
total = 0

# Count ratings.
count = 0

for row in ratings:

    for rating in row:

        print(rating, end=" ")

        total += rating

        # Count one rating.
        count += 1

    print()

print("\nTotal Rating =", total)
print("Number of Ratings =", count)