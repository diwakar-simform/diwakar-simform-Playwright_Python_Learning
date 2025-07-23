# 1. - Word frequency counter

from collections import Counter  # Counter is a subclass of dict that helps count hashable objects.
# It is useful for counting the frequency of words in a text.
def word_frequency_counter(text):
    words = text.split() # split the text into words
    print("Words = ", words) # Display the list of words
    print(type(words))  # Display the type of words variable
    frequency = Counter(words) # count the frequency of each word
    return frequency

print("Count = ",word_frequency_counter("Diwakar Kumar is a good QA Engineer. Diwakar Kumar is a good person."))

# another way to count the frequency of words

text = "Diwakar Kumar is a good QA Engineer. Diwakar Kumar is a good person."
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1  # get the current count of the word, if not found, return 0 and add 1 to it
print("Frequency = ", frequency)

# 2. - Remove duplicates

numbers = [1, 2, 3, 4, 5, 1, 2, 3]
print("Original numbers:", numbers)
# Using set to remove duplicates
unique_numbers = list(set(numbers))  # Convert to set to remove duplicates, then back to list
print("Unique numbers:", unique_numbers)


			
# - Address book dictionary

address_book = {
    "Alice": "123 Main St",
    "Bob": "456 Park Ave"
}

# Add new contact
address_book["Charlie"] = "789 Oak Rd"
address_book["Diwakar"] = "Nehrunagar, Ahemdabad"

# Display all contacts
for name, address in address_book.items():
    print(f"{name}: {address}")


