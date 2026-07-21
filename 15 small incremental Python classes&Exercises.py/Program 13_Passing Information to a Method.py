# Exercise 1 - Create a class called Speaker.
# Create a method called talk(message).
# Call the method three times using different messages.

class Speaker:
    
    def talk(self, message):
        print(message)

speaker1 = Speaker()
speaker2 = Speaker()
speaker3 = Speaker()

speaker1.talk("Hello World")
speaker2.talk("My name is Aoi")
speaker3.talk("Python is fun.")

# Exercise 1 - Create a class called Calculator.
# Create a method called show(number).
# Pass different numbers to the method.

class Calculator:
    def show(self, number):
        print(number)

calculator1 = Calculator()
calculator2 = Calculator()
calculator3 = Calculator()

calculator1.show(54)
calculator2.show(6777)
calculator3.show(2355)