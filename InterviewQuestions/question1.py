# Question1: 00:00 - What is the difference between a list and a tuple?
# Lists are mutable, and tuples are immutable

my_List = [1,3,4]

print("Original List = ", my_List)

my_List[0] = 2

# if you want to add anything to your list at the end you can use below method
my_List.append("at the end")

print("Changed List = ", my_List)

my_List.pop() # this will remove the last index value
my_List.pop(1) # this will remove the mentioned index number value

print("After using pop method on list = ", my_List)

my_tuple = (1, 2, 3)

print("Original Tuple = ", my_tuple)

# my_tuple[0] = 2 ------this is not allowd in tuples

print("Modified tuple = ", my_tuple)

