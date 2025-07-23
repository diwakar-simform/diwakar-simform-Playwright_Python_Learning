# Just like we have array in other programming languages, in Python we have a list. But the list can contain different data types collection unlike array.
# Also keep in mind that list has square brackets [] and tuple has round brackets ().
# Only difference between tuple and list is: list = mutable and tuple = immutable
myList = [1, 2.5, "Hello", True, None] 

print("myList[0] = ",myList[0])
print("myList: ",myList)

# if you want print last index value of the list, you can use negative indexing

print(myList[-1])  # prints None, which is the last element in the list

print(myList[1:3])  # prints [2.5, 'Hello'], which is a slice of the list from index 1 to 2 (3 is not included)

myList.append("New Item")  # adds a new item to the end of the list
myList.insert(2, "Inserted Item")  # inserts a new item at index 2

print(myList)  # prints the updated list

myList.remove("Hello")  # removes the first occurrence of "Hello" from the list
print(myList)  # prints the list after removing "Hello"
myList.pop()  # removes the last item from the list and returns it
print(myList)  # prints the list after removing items

myList.extend([10, 20, 30])  # adds multiple items to the end of the list
print(myList)  # prints the list after extending it with new items
myList += [40, 50]  # another way to add multiple items to the list
print(myList)  # prints the list after adding more items
# myList.sort()  # sorts the list in ascending order (works for numbers and strings)
# print(myList)  # prints the sorted list
myList.reverse()  # reverses the order of the list
print(myList)  # prints the reversed list
print(myList.count(10))  # counts how many times 10 appears in the list
print(myList.index(20))  # finds the index of the first occurrence of 20 in the list
myList.copy()  # creates a shallow copy of the list
myList[2] = "Modified Item"  # modifies the item at index 2
print(myList)  # prints the modified list
del myList[0]  # deletes the item at index 0
print(myList)  # prints the list after deleting the first item
myList.pop(1)  # removes the item at index 1 and returns it
print(myList)  # prints the list after popping the item at index 1
# myList.remove(30)  # removes the first occurrence of 30 from the list
print(myList)  # prints the list after removing 30
# del myList  # deletes the entire list
# print(myList)  # this will raise an error because myList is deleted
myList.clear()  # removes all items from the list
print(myList)  # prints the empty list after clearing it

