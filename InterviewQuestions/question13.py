# Question 13: 55:46 - How do you reverse the elements of a list?

# In Python, there are multiple ways to reverse the elements of a list. Here are the most common and interview-friendly methods:

# ✅ 1. Using reverse() method (In-place)
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]
# Modifies the original list
# Doesn’t return a new list

# ✅ 2. Using slicing [::-1] (Creates new reversed list)
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
# Does not modify the original list
# Common and very readable

# ✅ 3. Using reversed() with list()
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
# reversed() returns an iterator

# Use list() to convert it to a list

# 🧠 Summary Table:
# Method	      In-place	    Returns New List	    Best For
# list.reverse()	✅ Yes	    ❌ No	            When original list can be changed
# list[::-1]	    ❌ No	    ✅ Yes	            When you need a reversed copy
# reversed()	    ❌ No	    ✅ Yes (             with list())	When working with iterators