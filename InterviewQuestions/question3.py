# Question3: 06:27 - How do you implement inheritance and super keyword in Python?

class Parent:
    def greet(self):
        return "Hello from Parent Class"
    
class Child(Parent):
    def helloGreet(self):
        return "Hello from Child class"
    
c = Child()

print("Calling child class method from child class", c.helloGreet())

print("Calling Parent Class method from child class", c.greet())


class Parent1:
    def greeting(self):
        return "Hello from PARENT class"
    
class Child1(Parent1):
    def greeting(self):
        return super().greeting() + " + Hello from CHILD class"
    
c = Child1()

print("Calling parent class method using super keyword = ", c.greeting())