# Question14: 57:17 - Explain the difference between @classmethod and instance methods.

class MyClass:
    @classmethod
    def classMethod(cls):
        return "Hi, I am a class method"
    
    def instanceMethod(self):
        return "Hi, I am an instance method"
    

obj = MyClass()

print(obj.instanceMethod())
print(obj.classMethod()) # note: you can call a class method with obj
# print(MyClass.instanceMethod()) # note: but not the instance method with class name it will throw you the self error
print(MyClass.classMethod())


# class methods are like Static methods in other languages