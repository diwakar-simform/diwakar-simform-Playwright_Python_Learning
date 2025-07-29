#Question12: 52:07 - Why is the Self convention used in Python? Explain with an example.
# ✅ Why is self used in Python?
# In Python, self is a convention used inside class methods to refer to the instance of the class itself.
# self must be the first parameter of all the instance methods
# Whenever you create an object and call its method, Python automatically passes the object as the first argument to the method. By convention, we name this first argument self.
# Unlike other languages like c++, java++, Python does not have an explicit this keyword. Instead self is used to access instance variable and methods inside the class.

class Person:
    def __init__(self, name, age):
        self.name = name   # self.name is instance variable
        self.age = age     # self.age is instance variable

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Create object
p1 = Person("Diwakar", 25)
p1.greet()   # Output: Hi, I'm Diwakar and I'm 25 years old.
