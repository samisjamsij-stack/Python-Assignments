# Task 9 - Calculate Discounted Price 

# Formula - Final Price = Price - Discount
# Exercise 
# def discount_price(price, discount):
#   return price - discount
# final_price = discount_price(150, 20)
# print("Final Price: $", final_price)

# Exercise 1
def discount_price(price, discount):
    return price - discount

final_price = discount_price(150, 20)
print("Final Price: $", final_price)

# Exercise 2

def discount_price():

    price = float(input("Enter Price: "))
    discount = float(input("Enter Discount: "))

    final_price = price - discount
    print("Final Price: ", final_price)
    return final_price
discount_price()

# Exercise 3

def discount_price():

    subtotal = 0
    for i in range(1,5):

        product_name = str(input("Product Name: "))
        price = float (input("Enter price: "))
        discount = float(input("Enter Discount: "))

        final_price = price - discount

        subtotal += final_price
        print(f"Product Name: {product_name}\nPrice {price}\n Discount{discount}\n Final Price{final_price}\n")

    print("Subtotal: ", final_price)
discount_price()