from Chef import Chef

class Resturant:

    def __init__(self):
        self.chef = Chef()

    def serve_food(self):
        self.chef.cook()
        print("Food is served.")
