# Question19: 01:08:07 - How to Handle Exceptions in Python? Where does the finally keyword come into play with exceptions?

# 🔁 Without with (manual approach):
file = open("test.txt", "r")
try:
    data = file.read()
finally:
    file.close()  # You must remember to close it

# in case file is not present

try:
    with open("example.txt", "r") as file:
        data = file.read()
except FileNotFoundError as fe:
    print(fe)
finally:
    print("This is finally block")
    print("generally this is used for closing db connection, clean up resources")

# File is automatically closed after this block
