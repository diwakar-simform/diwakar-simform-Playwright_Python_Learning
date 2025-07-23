# functions in python
# functions are blocks of reusable code that perform a specific task. They help in organizing code, making it more readable and maintainable.

input = input("Enter your name: ")  # taking input from user

name = input.strip()  # removing leading and trailing spaces from the input

def greetMe(name):
    """
    This function takes a name as input and prints a greeting message.
    :param name: str
    """
    print(f"Hello, {name}!")
    print("Your FullName is: ", name, "Kumar")  # prints the full name
greetMe(name)  # calling the function with the input name


def sayHello():
    print("Hello, World!")  # prints a simple greeting message
sayHello()  # calling the function to print the greeting message

def sumOfTwoNumbers(a,b):
    print("Sum of", a, "and", b, "is:", a + b)  # prints the sum of two numbers
sumOfTwoNumbers(5, 10)  # calling the function with two numbers

def summation(a,b,c):
    return a + b + c  # returns the sum of three numbers

print("Summation of 5, 10, and 15 is:", summation(5, 10, 15))  # calling the function and printing the result