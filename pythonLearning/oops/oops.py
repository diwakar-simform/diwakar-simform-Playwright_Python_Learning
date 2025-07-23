# OOPs stands for Object-Oriented Programming, which is a programming paradigm based on the concept of "objects".
# Objects can contain data in the form of fields (often known as attributes) and code in the form of procedures (often known as methods).
# OOPs allows for code reusability, encapsulation, inheritance, and polymorphism.
# In Python, everything is an object, and Python supports OOPs concepts like classes, objects, inheritance, encapsulation,
# and polymorphism. 
# Classes are blueprints for creating objects, and objects are instances of classes.

class Person:
    name = "Diwakar"  # class attribute or class variable
    age = 30  # class attribute

    # if don't define any constructor, Python will create a default constructor for the class

    # instanace attributes are defined in the constructor (__init__ method)
    # __init__ method is a special method that is called when an object is created from a class and allows the class to initialize the attributes of the class.
    # It is also known as the constructor in Python.
    # You can define multiple constructors in a class, but only one will be called when an object is created.
    # If you define multiple constructors, the last one defined will be used.
    # You can also use default arguments in the constructor to provide default values
    # for the attributes if no values are passed when creating an object.
    # Note: Python does not support method overloading like other languages, so you cannot have
    # multiple methods with the same name but different parameters in the same class.

    def __init__(self):
        """
        This is the constructor of the Person class.
        It initializes the attributes of the class.
        """
        self.name = "Diwakar Kumar"  # instance attribute
        self.age = 30  # instance attribute
        print("First Constructor called")  # this will be printed when the object is created


    # def __init__(self, name="Diwakar Kumar", age=30):
    #     print("Second Constructor called")  # this will be printed when the object is created

    def __str__(self):
        """
        This method returns a string representation of the Person object.
        :return: str
        """
        return f"Person(Name: {self.name}, Age: {self.age})"
    
    def __repr__(self):
        """
        This method returns a string representation of the Person object for debugging.
        :return: str
        """
        return f"Person(Name: {self.name}, Age: {self.age})"
    
    def __del__(self):
        """
        This method is called when the object is about to be destroyed.
        It can be used to perform cleanup actions.
        """
        print(f"Person object with name {self.name} is being deleted.")

    def __len__(self):
        """
        This method returns the length of the name attribute.
        :return: int
        """
        return len(self.name)
    
 
 # self is a reference to the current instance of the class. It is used to access variables that belong to the class.
 # It must be the first parameter of any function in the class, but it is not explicitly passed when calling the method.
 # It is automatically passed by Python when the method is called on an object of the class.
 # You can name it anything, but it is a convention to use self
 # It is used to access the attributes and methods of the class in Python.
 # It allows you to differentiate between instance variables and local variables.
 # It is also used to access the class variables and methods from within the class.
# In Java, C++, and other languages, self is like this keyword which refers to the current instance of the class.

    def getPersonName(self):
        """
        This method returns the name of the person.
        :return: str
        """
        return self.name
    
    def getPersonAge(self):
        """
        This method returns the age of the person.
        :return: int
        """
        return self.age
    
    def whatisYourName(self, lastName):
        """
        This method prints the name of the person.
        """
        print("My name is: ", self.name, lastName)  # prints the name of the person

        
    
# Creating an object of the Person class
person = Person()  # instantiating the class

# Accessing class attributes and methods using the object
print("Person Name: ", person.getPersonName())  # prints the name of the person
print("Person Age: ", person.getPersonAge())  # prints the age of the person   

print("directly getting the class attribute name: ", person.name)  # prints the name of the person
print("directly getting the class attribute age: ", person.age)  # prints the age of the person

print("calling the method of class: ", person.whatisYourName("Yadav"))  # prints the string representation of the person object

