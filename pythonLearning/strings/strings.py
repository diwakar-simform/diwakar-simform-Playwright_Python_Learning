str = "String Example"
str2 = "String Example 2"

print("String Concatenation: ", str+str2)  # Concatenates two strings
print("String Repetition: ", str * 2)  # Repeats the string
print("String is:", str)
print("String length is:", len(str)) # Returns the length of the string
# substring formula is str[start:end+1]
print("Substring: ", str[0:6])  # prints characters from index 0 to 5

print("First character of string: ", str[0]) # prints first character of string
print("Last character of string: ", str[-1]) # prints last character of string
print("String contains 'Example':", "Example" in str)  # Checks if substring is present in the string
print("String contains 'example':", "example" in str)  # Case-sensitive check
print("String starts with 'String':", str.startswith("String"))  # Checks if string starts with a specific substring
print("String ends with 'Example':", str.endswith("Example"))  # Checks if string ends with a specific substring
print("String split:", str.split(" "))  # Splits the string into a list of substrings based on space
print("String join:", " ".join(["Join", "these", "words"]))  # Joins a list of words into a single string with spaces
print("String find 'Example':", str.find("Example"))  # Finds the index of the first occurrence of a substring

print("String in uppercase:", str.upper())
print("String in lowercase:", str.lower())
print("String in title case:", str.title()) # Capitalizes the first letter of each word
print("String in capitalized case:", str.capitalize()) # Capitalizes the first letter of the string
print("String in swapcase:", str.swapcase()) # Swaps the case of each character in the string
print("String in reversed case:", str[::-1]) # Reverses the string
print("String with leading and trailing spaces removed:", str.strip())  # Removes leading and trailing spaces
print("String with leading spaces removed:", str.lstrip())  # Removes leading spaces
print("String with trailing spaces removed:", str.rstrip())  # Removes trailing spaces
print("String with 'Example' replaced by 'Demo':", str.replace("Example", "Demo"))  # Replaces a substring with another substring
print("String with 'Example' replaced by 'Demo' with count 1:", str.replace("Example", "Demo", 1))  # Replaces a substring with another substring, limited to 1 occurrence

