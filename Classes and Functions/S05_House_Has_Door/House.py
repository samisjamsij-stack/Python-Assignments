from Door import Door

class House:
    def __init__(self):
        self.door = Door()

    def enter(self):
        self.door.open()
        print("Welcome Home!")