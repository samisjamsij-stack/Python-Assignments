from Customer import Customer

class Bank_Account:

    def __init__ (self):
        self.customer = Customer()

    def display_account(self):
        self.customer.show_name()
        print("Balance: $500")