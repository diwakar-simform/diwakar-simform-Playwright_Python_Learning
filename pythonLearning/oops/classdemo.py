# self keyword is mandatory for calling variables in method
# Instance and class variable have whole different purpose
# class variables are like static variable in other languages.
# construct name should be __init__(self) in python, it is called when the object is created.


class Number:
    number1 = 10
    number2 = 20

    def __init__(self):
        # This is a constructor, it is called when the object is created
        print("Constructor called, object created with number1 =", self.number1, "and number2 =", self.number2)

    def sumOfTwoNum(self):
        summation = self.number1 + self.number2
        print("Summation of ",self.number1, "&",self.number2," is equal to ",summation)
        return summation

    def addTwoNum(self, a, b):
        return a+b


numbers = Number() # new keyword is not required in python to create an object

print("sum of two number",numbers.sumOfTwoNum())

print("addition of two num", numbers.addTwoNum(50,50))