# this one is dedicated to loops in python
# loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# Python has two main types of loops: `for` loops and `while` loops.
# 1. For Loop
# A `for` loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.

obj = [1,2,3,4,5]
j = 1
for i in obj: # iterating over the list obj using a for loop
    print(j," object of the list: ",i)  # prints each element in the list
    j += 1 # incrementing j by 1 in each iteration
     
# iterating over a range of numbers from 1 to 5     
for i in range(1, 6):  # range (i,j) generates numbers from i to j-1
    print("Number: ", i)  # prints each number in the range

# sum of numbers from 1 to 5 using a for loop
sum = 0
for i in range(1, 6):
    sum += i  # adds each number to the sum

print("Sum of numbers from 1 to 5: ", sum)  # prints the sum

# If you want to iterate over a list of strings
names = ["Alice", "Bob", "Charlie","David", "Eve"]
for name in names:
    print("Name: ", name)  # prints each name in the list
# You can also use a for loop with the `enumerate()` function to get both the index and value
for index, value in enumerate(names):
    print(f"Index: {index}, Name: {value}")  # prints the index and name

# if you want to jump the every 2 index of the loop
for i in range(0, len(names), 2):  # step of 2
    print("Name at index", i, ":", names[i])  # prints every second name

for i in range(1, 10, 2):
    print("Odd number:", i)  # prints odd numbers from 1 to 9

for i in range(2, 11, 2):
    print("Even number:", i)  # prints even numbers from 2 to 10

for i in range(1, 11,6):
    print("Number with step of 6:", i)  # prints numbers with a step of 6

for i in range(10):
    print("Number from 0 to 9:", i)  # prints numbers from 0 to 9