# Step 2 - Find Total Rating

ratings = [
    [5, 4, 5],
    [3, 5, 4],
    [5, 5, 5]
]

# Store the total.
total = 0

# Loop through each row.
for row in ratings:

    # Loop through each rating.
    for rating in row:

        # Display the rating.
        print(rating, end=" ")

        # Add the rating to the total.
        total += rating

    print()

# Display total.
print("\nTotal Rating =", total)