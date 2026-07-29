# Example
cash = 2350
invoice = 400

paid_invoices = cash // invoice
remaining_cash = cash % invoice

print("Invoices Paid:", paid_invoices)
print("Cash Left:", remaining_cash)

# Task 1
pay_invoices = 1875
invoice_costs = 250

invoices_paid = pay_invoices // invoice_costs
cash_left = pay_invoices % invoice_costs

print("Invoices Paid:", invoices_paid)
print("Cash Left:", cash_left)

if invoices_paid == 0:
    print("There is no money remaining after paying invoices.")
else:
    print("There is money remaining after paying invoices.")

# Task 2
pay_suppliers = 3460
supplier_bill = 600

bills_paid = pay_suppliers // supplier_bill
cash_left = pay_suppliers % supplier_bill

print("Bills Paid:", bills_paid)
print("Cash Left:", cash_left)

if bills_paid == 0:
    print("All cash has been used to pay suppliers.")
else:
    print("Some cash remains after paying suppliers.")

# Task 3
rent_payment = 5125
rent_installment = 700

installments_paid = rent_payment // rent_installment
cash_left = rent_payment % rent_installment

print("Installments Paid:", installments_paid)
print("Cash Left:", cash_left)

if installments_paid == 0:
    print("All installments have been paidwith no remaining funds.")
else:
    print("Money is left after paying rent..")

# Task 4
advertisement_budget = 940
campaign_cost = 125

campaigns_paid = advertisement_budget // campaign_cost
cash_left = advertisement_budget % campaign_cost

print("Campaigns Funded:", campaigns_paid)
print("Remaining Budget:", cash_left)

if campaigns_paid == 0:
    print("All campaigns have been funded.")
else:
    print("Some advertising funds remain.")

# Task 5
utility_bills = 2760
bill_cost = 350

bills_paid = utility_bills // bill_cost
cash_left = utility_bills % bill_cost

print("Bills Paid:", bills_paid)
print("Cash Left:", cash_left)

if bills_paid == 0:
    print("All utility bills have been paid with no remaining funds.")
else:
    print("Some cash remains after paying utility bills.")

# Task 6
maintenance_funds = 1305
service_costs = 150

visits_paid = maintenance_funds // service_costs
cash_left = maintenance_funds % service_costs

print("Visits Paid:", visits_paid)
print("Cash Left:", cash_left)

if visits_paid == 0:
    print("All maintenance services have been paid for.")
else:
    print("Maintenance budget still has money left.")

# Task 7
employees_paid = 4835
salary_payment = 750

salaries_paid = employees_paid // salary_payment
cash_left = employees_paid % salary_payment

print("Salaries Paid:", salaries_paid)
print("Cash Left:", cash_left)

if salaries_paid == 0:
    print("All salaries have been paid.")
else:
    print("Not enough money to pay another employee.")

# Task 8
computers_purchased = 1220
computer_costs = 290

computers_bought = computers_purchased // computer_costs
cash_left = computers_purchased % computer_costs

print("Computers Bought:", computers_bought)
print("Cash Left:", cash_left)

if computers_bought == 0:
    print("No computers were bought.")
else:
    print("Money remains after buying computers.")

# Task 9
raw_materials = 3150
batch_costs = 425

batches_bought = raw_materials // batch_costs
cash_left = raw_materials % batch_costs

print("Batches Produced:", batches_bought)
print("Cash Left:", cash_left)

if batches_bought == 0:
    print("No raw material purchases were made.")
else:
    print("Money remains for future purchases.")

# Task 10
contractor_fees = 2995
each_contractor_fee = 500

contractors_fees_paid = contractor_fees // each_contractor_fee
cash_left = contractor_fees % each_contractor_fee

print("Contractors Paid:", contractors_fees_paid)
print("Cash Left:", cash_left)

if contractors_fees_paid == 0:
    print("No contractor fees have been paid.")
else:
    print("There is not enough money to pay another contractor.")