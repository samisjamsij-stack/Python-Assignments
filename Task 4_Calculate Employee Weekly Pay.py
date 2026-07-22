# Task 4 - Calculate Employee Weekly Pay

# Exercise 1
def weekly_pay(hours, rate):
    return hours * rate

pay = weekly_pay(40,22)
print("Weekly Pay = $", pay)

# Exercise 2 

def weekly_income(hours, rate):
    return hours * rate

employee = input("Employee Name: ")
rate = float(input("Hourly Rate: "))
hours = float(input("Hours Worked: "))

weekly_pay = weekly_income(hours, rate)

print("Employee Name: ", employee)
print("Weekly pay = $ ", weekly_pay)

# Exercise 3 - Calculate the weekly pay for three employees.
def weekly_pay(hours, rate):
    return hours * rate

grand_total = 0

for employee in range(1,4):
    print("Employee", employee)

    name = input("Name: ")
    hours = float(input("Hours: "))
    rate = float(input("Rate: "))

    pay = weekly_pay(hours, rate)
    print(name, "Weekly Pay =$", pay)

    grand_total +=pay
print("Grand Payroll = $ ", grand_total)
