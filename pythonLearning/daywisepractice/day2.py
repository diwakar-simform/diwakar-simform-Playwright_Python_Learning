# - Largest of 3 numbers

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

if num1 >= num2:
    if num1 >= num3:
        print(num1, "is greater among all three numbers")
    else:
        print(num3, "is greater among all three numbers")
elif num2 >= num3:
    print(num2, "is greater among all three numbers")
else:
    print(num3, "is greater among all three numbers")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 2. Grade Calculator

marks = float(input("Please enter your marks: "))

if marks <= 100 and marks >= 80:
    print("Grade: A")
elif marks < 80 and marks >= 60:
    print("Grade: B")
elif marks < 60 and marks >= 40:
    print("Grade: C")
elif marks < 40 and marks >= 30:
    print("Grade: D")
else:
    print("Grade: F")

# 3. Simple Login Validation

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == "diwakar" and password == "1234":
    print("You are logged in successfully as ", username)
else:
    print("Invalid username or password. Please try again.")