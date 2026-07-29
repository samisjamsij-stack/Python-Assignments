# Task 6 - Convert Hours to Minutes

# Exercise 1 - Convert 5 hours into minutes.
def hours_to_minutes(hours):
    return hours * 60

minutes = hours_to_minutes(5)
print("Minutes = ", minutes)

# Exercise 2 - Ask the user to enter the number of hours.
def hours_to_minutes(hours):
    return hours * 60

hours = float(input("Enter hours: "))
minutes = hours_to_minutes(hours)

print("Hours: ", hours)
print("Minutes: ", minutes)

# Exercise 2 - Ask the user to enter the number of hours.

def hours_to_minutes(hours):
    return hours * 60

hours = float(input("Enter hours: "))
minutes = hours_to_minutes(hours)

print("Hours: ", hours)
print("Minutes: ", minutes)

# Exercise 3 - Return both minutes and seconds.

def time_converter(hours):
    minutes = hours * 60
    seconds = hours * 3600
    return minutes, seconds

hours = float(input("Enter hours: "))
minutes, seconds = time_converter(hours)

print("Hours: ", hours)
print("Minutes: ", minutes)
print("Second: ", seconds)