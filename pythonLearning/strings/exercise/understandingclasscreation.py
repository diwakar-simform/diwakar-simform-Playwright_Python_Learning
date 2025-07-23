# Understanding class creation in Python
# Objective: Create a basic calculator class to perform addition, subtraction, multiplication, and division.

# Instructions:

# Create a class named BasicCalculator.

# Define a constructor that initializes two numbers. Use numbers 10 & 5

# Implement methods for:

# Addition

# Subtraction

# Multiplication

# Division

# Each method should return the result of the operation.

# Create an instance of the BasicCalculator class and demonstrate the functionality of each method.

# Example Output:

# Addition: 10 + 5 = 15
# Subtraction: 10 - 5 = 5
# Multiplication: 10 * 5 = 50
# Division: 10 / 5 = 2.0


class BasicCalculator:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def addition(self):
        return self.num1+self.num2
    
    def subtraction(self):
        return self.num1 - self.num2
        
    def multiplication(self):
        return self.num1 * self.num2
    def division(self):
        return self.num1 / self.num2
        
calculate = BasicCalculator(10,5)

print("Addition: 10 + 5 =", calculate.addition())

print("Subtraction: 10 - 5 =", calculate.subtraction())

print("Multiplication: 10 * 5 =", calculate.multiplication())

print("Division: 10 / 5 =", calculate.division())