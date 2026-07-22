'''Task 9 - Calculate Simple Interest
Interest = (Principal * Rate * Time) / 100

Example: 
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
interest = simple_interest(5000, 6, 3)
print("Interest: ", interest)'''

# Exercise 1

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
interest = simple_interest(4000, 5, 4)
print("Interest: ", interest"\n")

# Exercise 2

def simple_int():
    
    principal = float(input("Enter Price: "))
    rate = float(input("Enter Discount: "))
    time = float(input("Time: "))

    simple_int = principal * rate * time / 100

    print("Princpal: ", principal)
    print("Rate: ", rate, "%")
    print("Time: ", time, "Years")

    return simple_int
simple_int()

# Exercise 3

def final_amo():
    
    principal = float(input("Principal: "))
    rate = float(input("Rate: "))
    time = float(input("Time: "))

    simple_int = principal * rate * time / 100
    final_amo = principal + interest

    print(f"Principal: {principal}\nRate: {rate}\n Time: {time}\n")
    return final_amo , simple_int
final_amo()
