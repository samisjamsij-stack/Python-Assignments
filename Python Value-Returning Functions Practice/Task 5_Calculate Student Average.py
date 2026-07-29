# Task 5 Calculate Student Average

# Exercise 1
def average(score1, score2, score3):
    return (score1, score2, score3) / 3

result = average(80, 90, 100)
print("Average = ", result)

# Exercise 2 - Ask the user for five subject scores. Return the average.

def student_average(S1, S2, S3, S4, S5):
    return (S1 + S2 + S3 + S4 + S5) / 5

english = float(input("English: "))
math = float(input("Math: "))
science = float(input("Science: "))
history = float(input("History: "))
biology = float(input("Biology: "))

student_average = average(
    english,
    math,
    science,
    history,
    biology

)

print("Average = ", student_average)

# Exercise 3 - Display the grade and average.
def student_average(S1, S2, S3, S4, S5):
    return (S1 + S2 + S3 + S4 + S5) / 5

english = float(input("English: "))
math = float(input("Math: "))
science = float(input("Science: "))
history = float(input("History: "))
biology = float(input("Biology: "))

student_average = average(
    english,
    math,
    science,
    history,
    biology
)

if student_average >= 90:
    grade = "A"
elif student_average >= 80:
    grade = "B"
elif student_average >= 70:
    grade = "C"
elif student_average >= 60:
    grade = "D"
else:
    grade = "F"

print("\nAverage =", round(student_average, 2))
print("Grade =", grade)
