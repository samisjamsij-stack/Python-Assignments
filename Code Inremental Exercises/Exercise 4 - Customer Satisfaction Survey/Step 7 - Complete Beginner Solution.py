# Step 7 - Complete Customer Ratings Report

ratings = [
    [5, 4, 5],
    [3, 5, 4],
    [5, 5, 5]
]

# 1. Store the total rating.
total = 0

# 2. Count the number of ratings.
count = 0

# 3. Count perfect ratings.
perfect = 0

# 4. Loop through each customer's ratings.
for row in ratings:

    # 5. Loop through each rating.
    for rating in row:

        # 6. Display the rating.
        print(rating, end=" ")

        # 7. Add the rating to the total.
        total += rating

        # 8. Count the rating.
        count += 1

        # 9. Check for a perfect rating.
        if rating == 5:

            # 10. Increase the perfect rating counter.
            perfect += 1

    # 11. Move to the next row.
    print()

# 12. Calculate the average.
average = total / count

# 13. Display the average.
print("\nAverage Rating =", round(average, 2))

# 14. Display perfect ratings.
print("Perfect Ratings =", perfect)