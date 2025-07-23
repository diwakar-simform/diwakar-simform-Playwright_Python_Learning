# Working with Lists
# Create a list named fruits that contains below five different fruit names (strings).

# "apple", "banana", "cherry", "date", "elderberry"
# Print the first and last elements of the list.

# Use slicing to print the second and third fruits from the list.

# Expected Result:

# First fruit: apple
# Last fruit: elderberry
# Fruits from index 1 to 2: ['banana', 'cherry']

list = ["apple", "banana", "cherry", "date", "elderberry"]

print("First fruit:",list[0])

print("Last fruit:", list[len(list)-1])

print("Fruits from index 1 to 2:",list[1:3])

