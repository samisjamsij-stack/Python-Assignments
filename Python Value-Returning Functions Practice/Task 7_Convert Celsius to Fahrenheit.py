# Task 7 - Convert Celsius to Fahrenheit
# Formula
# F = (C x 9 / 5) + 32
# Example: 
def celsius_to_fahrenheit(celsius):
   return (celsius * 9 / 5) + 32
temperature = celsius_to_fahrenheit(25)
print("Temperature: ", temperature)

# Exercise 1

def C_t_F(celsius):
   return (celsius * 9 /5) + 32
temperature = celsius_to_fahrenheit(30)
print("Temperature: ", temperature)

# Exercise 2
temperature = float(input("Enter Celsius: "))

def celsius_to_fahrenheit():
   return (temperature * 9 / 5) + 32

fahrenheit = celsius_to_fahrenheit()

print("Celsius: = ", temperature)
print("Fahrenheit: ", celsius_to_fahrenheit())

# Exercise 3

def celsius_to_fahrenheit(celsius):

   weather = ""

   for i in range(3):

      if celsius <= 0:
         weather = "Freezing"
      elif celsius <= 15:
         weather = "Cold"
      elif celsius <= 30:
         weather = "Warm"
      else: 
         weather = "Hot"

   print("Clesius: ", celsius)
   print("Weather: ", weather)
   
   return (celsius * 9 / 5) + 32

celsius = float(input("Enter Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Fahrenheit: ", fahrenheit)
