# - calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Example usage:
print("Add:", add(10, 5))         # 15
print("Subtract:", subtract(10, 5)) # 5
print("Multiply:", multiply(10, 5)) # 50
print("Divide:", divide(10, 5))   # 2.0
print("Divide:", divide(10, 0))   # Cannot divide by zero

# - Prime checker

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1): # We loop from 2 to square root of n (faster than checking all the way to n).
        if n % i == 0:
            return False
    return True

# Example usage:
num = 11
if is_prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")


# - Division with exception handling

def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print(safe_division(10, 2))   # 5.0
print(safe_division(10, 0))   # Error: Cannot divide by zero


