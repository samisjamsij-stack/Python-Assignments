# 1. Write a program that declares 1 variable x, and then assigns 7 to it. 
# Write an if statement to print out “Less than 10” if x is less than 10. 
x = 7 

if x < 10: 
    print("Less than 10")

# 1b. Change x to equal 15, and notice the result
# (the console should not display anything).
x = 15 

if x < 10: 
    print("Less than 10")

# 2. Write a program that declares 1 variable x, and then assigns 7 to it.
# Write an if-else statement that prints out “Less than 10” if x is less than 10,
# and “Greater than 10” if x is greater than 10.
x = 7

if x < 10:
    print("Less than 10")
else:
    x > 10
    print("Greater than 10")

# 2b. Change x to 15 and notice the result.
x = 15

if x < 10:
    print("Less than 10")
else:
    x > 10
    print("Greater than 10")

# 3. Write a program that declares 1 variable x, and then assigns 15 to it.
# Write an if...elif...else statement that prints out “Less than 10” if x is less than 10; “Between 10 and 20” 
# if x is greater than 10 but less than 20, and “Greater than or equal to 20” if x is greater than or equal to 20.
x = 15

if x < 10:
    print("Less than 10")
elif x > 10 and x < 20:
    print("Between 10 and 20")
else:
    x <= 20
    print("Greater than or equal to 20")

# 3b. Change x to 50 and notice the result.
x = 50

if x < 10:
    print("Less than 10")
elif x > 10 and x < 20:
    print("Between 10 and 20")
else:
    x <= 20
    print("Greater than or equal to 20")

# 4. Write a program that declares 1 variable x, and then assigns 15 to it.
# Write an if-else statement that prints “Out of range” if the number is less than 10 or greater than 20.
# And prints “In range” if the number is between 10 and 20 (including equal to 10 or 20).
x = 15

if x < 10 or x > 20:
    print("Out of Range")
else:
    x > 10 and x <= 20
    print("In range")

# 4b. Change x to 5 and notice the result. 
x = 5

if x < 10 or x > 20:
    print("Out of Range")
else:
    x > 10 and x <= 20
    print("In range")

# 5. Write a program that uses if...elif...else statements to print out grades A, B, C, D, and F according to the following criteria:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: <60

score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif 60 < score:
    print("F")
else:
    score < 0 or score > 100
    print("Score out of range")

#  6. Create a program that lets the users input their filing status and income.
# Display how much tax the user would have to pay according to status and income.

income = float(input("Enter income balance: "))
marriage_status = input("Enter marriage Status: Single, Married Filing Jointly/Window, Married Filing Separately, Head of Household): ")

if marriage_status == "Single":
    if income <= 8350.0:
        print("Marginal Tax Rate: 10%")
    elif income >= 8351.0 or income <= 33950.0:
        print("Marignal Tax Rate: 15%")
    elif income >= 33951.0 or income <= 82250.0:
        print("Marginal Tax Rate: 25%")
    elif income >= 82251.0 or income <= 171550.0:
        print("Marginal Tax Rate: 28%")
    elif income >= 171551.0 or income <= 372950.0:
        print("Marginal Tax Rate: 33%")
    elif income >= 372951.0:
        print("Marginal Tax Rate: 35%")
else:
    print("Invalid entry")

if marriage_status == "Married Filing Jointly/Window":
    if income <= 16700:
        print("Marginal Tax Rate: 10%")
    elif income >= 16701 or income <= 67900:
        print("Marignal Tax Rate: 15%")
    elif income >= 67901 or income <= 137050:
        print("Marginal Tax Rate: 25%")
    elif income >= 137051 or income <= 208850:
        print("Marginal Tax Rate: 28%")
    elif income >= 208851 or income <= 372950:
        print("Marginal Tax Rate: 33%")
    elif income >= 372951:
        print("Marginal Tax Rate: 35%")

if marriage_status == "Married, Filing Separately":
    if income <= 8350:
        print("Marginal Tax Rate: 10%")
    elif income >= 8351 or income <= 33950:
        print("Marignal Tax Rate: 15%")
    elif income >= 33951 or income <= 68525:
        print("Marginal Tax Rate: 25%")
    elif income >= 68526 or income <= 104425:
        print("Marginal Tax Rate: 28%")
    elif income >= 104426 or income <= 186475:
        print("Marginal Tax Rate: 33%")
    elif income >= 186476:
        print("Marginal Tax Rate: 35%")

if marriage_status == "Head of Household":
    if income <= 11950:
        print("Marginal Tax Rate: 10%")
    elif income >= 11951 or income <= 45500:
        print("Marignal Tax Rate: 15%")
    elif income >= 45501 or income <= 117450:
        print("Marginal Tax Rate: 25%")
    elif income >= 117451 or income <= 190200:
        print("Marginal Tax Rate: 28%")
    elif income >= 190201 or income <= 372950:
        print("Marginal Tax Rate: 33%")
    elif income >= 372951:
        print("Marginal Tax Rate: 35%")