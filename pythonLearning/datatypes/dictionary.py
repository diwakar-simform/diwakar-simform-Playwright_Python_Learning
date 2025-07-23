# dictionary data type is a collection of key-value pairs. it is similar to a hashmap in other programming languages.

# In Python, dictionaries are defined using curly braces {} and key-value pairs are separated by commas.
# Keys must be unique and immutable (strings, numbers, or tuples), while values can be of any data type.
# Below are the Example of a dictionary with string keys and values, and an integer key

dictionary = {  
    "name": "John",
    "age": 30,
    "city": "New York",  # double quotes are used for string values only no matter it is key or value
    1: "apple",
}

print("dictionary['name'] = ", dictionary["name"])  # accessing value by key' make string value is in double qoutes
print("dictionary: ", dictionary)  # prints the entire dictionary
print(dictionary[1])  # accessing value by key, here key is an integer

# How to create dictionary at runtime and add data into it:
# These empty dictionary helps us in loading excel data into a dictionary

dict = {} # this is how we represents an empty dictionary

print("dict: ", dict)  # prints the empty dictionary

dict["name"] = "Alice"  # adding key-value pair
dict["age"] = 25  # adding another key-value pair
dict[4] = "banana"  # adding another key-value pair with integer key

print("dict after adding data: ", dict)  # prints the dictionary after adding data