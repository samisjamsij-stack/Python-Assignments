# Step 1 - Display Customer Ratings

ratings = [
    [5, 4, 5],
    [3, 5, 4],
    [5, 5, 5]
]

# Loop through each row.
for row in ratings:

    # Loop through each rating.
    for rating in row:

        # Display each rating.
        print(rating, end=" ")

    # Move to the next line.
    print()