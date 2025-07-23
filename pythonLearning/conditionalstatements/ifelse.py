# if else is used to check the condition and execute the code based on the condition
# here you will understand how indentation is important in python
# indentation means the space before the code, it defines the scope of the code block
# colon (:) is used to define the start of the code block

greeting = "Good Morning"

if greeting == "Good Mornig":
    print("Greeting is Good Morning")
else: 
    print("Greeting is not Good Morning")

print("outside if else block")

# condition match in if else block in python

a = 2.5

if a > 2:
    print("a is greater than 2")
elif a < 2:
    print("a is less than 2")
else:
    print("a is equal to 2")

