from classdemo import Number

class ChildClass(Number):
    var = 100

    def getVar(self):
        return self.var

# below code is used to test the ChildClass

cc = ChildClass()
print("Value of var in ChildClass:", cc.getVar())
cc.sumOfTwoNum()
print("addition of two num",cc.addTwoNum(30, 40))


class ChildClass2(Number):

    def __init__(self):
        Number.__init__(self) # Call the parent class constructor using the class name directly
    
    # Alternatively, you can use super() to call the parent class constructor
    # def __init__(self):
    #     super().__init__()  # Call the parent class constructor using super()
     
    classVar = 200
    def addParentVarWithChildVar(self):
        return self.classVar + self.number1
    

# below code is used to test the ChildClass2

cc2 = ChildClass2()

print("calling parent var in child var: ",cc2.addParentVarWithChildVar())
