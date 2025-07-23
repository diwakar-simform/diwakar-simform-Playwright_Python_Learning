# Count Lines in a File
# Objective: Count and print the number of lines in a file.

# Instructions:

# Use the attached text file "file1.txt"

# Write a Python script that opens the file, reads through it line by line, counts how many lines it has, and prints the total count.

# Expected result:

# Total number of lines: 5


with open('file1.txt','r') as file:
    content = file.readlines()
    print("Total number of lines:",len(content))