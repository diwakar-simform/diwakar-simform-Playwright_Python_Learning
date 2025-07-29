# Question9: 30:32 - What is lambda function in Python?

"""
    a lambda function in python is a small, anonymous function that can have multiple arguments but only one expression.

    It is written in a single line
    It is used where a short function is needed temporarily.
    Don't use lambda if the function is complex-use def instead.
"""


def add(x,y):
    return x+y

my_sum = lambda x,y : x+y

print("sum = ", my_sum(55,5))

numbersList = [0,1,2,3,4,5,6]

newNumberList = map(lambda x: x*3, numbersList) # this will go an iterave with each numbersList element and return data in raw format

print("New Number List = ", list(newNumberList)) # to convert from raw format to list we use list() function
print("numbersList = ", numbersList)

# filter valiues based on conditions

filterNumberList = filter(lambda x: x%2 == 0, numbersList)

print("filterNumberList = ", list(filterNumberList))

print("numberList = ", numbersList)