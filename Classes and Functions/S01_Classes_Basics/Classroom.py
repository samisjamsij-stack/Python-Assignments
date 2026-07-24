# 1. Import the Student class
from Student import Student

# 2. Create the Classroom class
class Classroom:

    # 3. Constructor
    def __init__(self):
        #Composition: Classroom has a Student object
        self.student = Student()

    # 4. Method
    def start_class(self):
        print("Class is starting...")
        self.student.say_hello()