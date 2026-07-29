'''Task 10 - Calculate the Accounting Equation

Formula: Assets = Liabilities + Equity

Example: 
def calculate_assets(liabilities, equity):
    return liabilites + equity

assets = calculate_assets(25000, 75000)
print("Assets: ", assets)'''

# Exercise 1

def calculate_assets(liabilities, equity):
    return liabilities + equity
    
assets = calculate_assets(40000, 60000)
print("Assets: ", assets)

# Exercise 2

def calculate_assets(l,e):
    return l + e

company_name = str(input("Enter Company Name: "))
l = float(input("Enter Liabilities: "))
e = float(input("Enter Equity: "))

assets = calculate_assets(l,e)

print(f"Company Name: {company_name}\nEquity: ${e}\n Assets: ${assets}\nLiabilities: ${l}")
    
print("Assets: ", assets)


# Exercise 3

