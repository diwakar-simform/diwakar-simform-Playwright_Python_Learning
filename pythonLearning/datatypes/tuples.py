# List data type is mutable, meaning you can change its content without changing its identity.
# Everything between tuple and list is same except for below mentioned things.
# Where tuple data type is immutable, meaning you cannot change its content once it is created.
# Another diffeerence is that tuple is faster than list because it is immutable.
# Tuples are used when you want to store a collection of items that should not change throughout the program.
# Tuples are defined using parentheses () and lists are defined using square brackets [].

myTuple = (1, 2.5, "Hello", True, None)
print("myTuple[0] = ", myTuple[0])

print("myTuple: ", myTuple)
print("count 1: ",myTuple.count(2.5))  # counts how many times 1 appears in the tuple

# myTuple[0]= 2 # this will raise an error because tuples are immutable