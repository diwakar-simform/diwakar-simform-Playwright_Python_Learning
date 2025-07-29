# Question2 = 05:04 - What are Python’s built-in data types?

a = 1 # int
b = {"a":12} # dictionary : Key Value pairs
c = "STRING" # string
d = 1.7 # float
e = True # boolean

# 🔸 Creating a Set
# A set is a built-in data type in Python that stores an unordered collection of unique items.
# ✅ Key Properties of a Set:
# Property	Description
# Unordered	No guaranteed order of elements
# No Duplicates	Every element is unique
# Mutable	You can add/remove elements after creation
# Iterable	Can loop through it using a for loop


my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# or using set() constructor
my_set = set([1, 2, 3, 3, 4])
print(my_set)  # Output: {1, 2, 3, 4}

# 🔹 Common Set Operations
# Operation	       Example	                   Description
# Add item	        my_set.add(5)	           Adds a new element
# Remove item	    my_set.remove(2)	       Removes a specific element
# Discard item	    my_set.discard(10)	       Same as remove, but no error if absent
# Union	           `a	bora.union(b)`
# Intersection	    a & b or a.intersection(b)	Common elements
# Difference	    a - b or a.difference(b)	Items only in a, not in b
# Clear all items	my_set.clear()	             Empties the set