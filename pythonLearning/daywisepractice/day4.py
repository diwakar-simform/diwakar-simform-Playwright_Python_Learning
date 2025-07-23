# 1. Reverse a list or string

list = [1,2,3,4,5,6,7,8,9,10]

print("Original List:", list)
print("Reversed List:", list[::-1])  # Using slicing to reverse the list, it does not change the original list
list.reverse()  # This will reverse the original list in place, # In-place reverse
print("Reversed List using reverse() method:", list)

str = "Hello, World!"
print("Original String:", str)
print("Reversed String:", str[::-1])  # Using slicing to reverse the string, but it does not change the original string
print(str)

# is there any way to reverse the original string? Strings in Python are immutable, meaning once a string is created, it cannot be changed in place.
# However, you can create a new reversed string using slicing or the `reversed()` function.
# If you assign the reversed result back to the original variable, that variable will point to a new string, but still the old string is not changed — it's just replaced:

reversed_str = ''.join(reversed(str))  # Using the reversed() function and join
print("Reversed String using reversed() function:", reversed_str)
print("Original String after reversing:", str)  # Original string remains unchanged



# 2. Count vowels

vowels = "aeiou"
strInput = input("Please enter your word to find the number of vowels: ")

# vowel_count = sum(1 for char in strInput if char in vowels)
# print(f"The number of vowels in '{strInput}' is: {vowel_count}")

count = 0
for char in strInput:
    if char.lower() in vowels:  # Using lower() to make the check case-insensitive
        count += 1

print(f"The number of vowels in '{strInput}' is: {count}")
    


# 3. Simple Contact Book

contacts = []

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})

def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            print("Name = ", contact["name"], "Phone = ", contact["phone"])

add_contact("John Doe", "123-456-7890")
add_contact("Jane Smith", "987-654-3210")
display_contacts()

print(contacts)  # Display the contacts list
print(type(contacts))  # Display the type of contacts variable

