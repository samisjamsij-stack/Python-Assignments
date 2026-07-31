# Step 5 - Round the Average

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

average = total / count

print("\nAverage Rating =", round(average, 2))