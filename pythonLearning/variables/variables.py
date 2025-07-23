# Code indentation is important in Python, it defines the scope of loops, functions, classes, etc.


a = 3 # a is a variable, in python variables are dynamic
print(a+3)

str = "Hello world"
print(str)

b,c, d = 1, 2, 3

print(b, c, d)

b,c,d = 4, 5.6, "Hello World"
print(b, c, d)

# print('value of b = '+b) incorrect way to concatenate string and integer

print("{}{}".format(d, c))  # correct way to concatenate string and integer

# How to know that the python is attaching what data type to a variable?

print(type(a), type(b), type(c), type(d))  # prints the data type of the variable