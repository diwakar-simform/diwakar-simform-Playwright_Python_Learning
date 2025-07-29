# Question4: 10:37 - What is init() in python?
# __init__() method is known as a constructor in OOP terminology. It is used to intialize an object's state when it is created. This method is automatically called when a new instance of a class is instantiated.

# if you don't declare __inti()__ method then it will call default constructor automatically.

class Constructors:
    def __init__(self, title):
        self.title = title

    def greet(self):
        return "greet()method + "+self.title
    

c = Constructors("title for instance variable")

print("greet() method ", c.greet())
