# Problem: Each number represents a customer satisfaction score (1-5)
# Display the scores.
# Count the number of perfect ratings (5).
# Calculate the average rating.

scores = [
    [5, 4, 5, 3],
    [4, 5, 5, 4],
    [3, 4, 4, 5]
]

perfect_ratings = 0
average = 0

for row in scores:
    for amount in row:
        average += amount
        amount += 1

for row in scores:
    for perfect_ratings in row:
        if amount >= 5:
            perfect_ratings + 1

average = average / amount

print("Average: ", average)
print("Perfect scores: ", perfect_ratings)