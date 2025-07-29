# Question8: 25:51 - How do you create a list of dictionaries in Python?
# List of dictionaries is nothing but a json file

list_of_dict = [
    {"One":1, "Two":2, "Three":3},
    {"Four":4, "Five": 5, "Six": 6}
]

print("First element of first list_of_dict: ", list_of_dict[0]["One"])
print("First element of second list_of_dict: ", list_of_dict[1]["Four"])

print("First list_of_dict", list_of_dict[0])
print("Second list_of_dict", list_of_dict[1])
