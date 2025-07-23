# with open('dummytext.txt') as file: # this is a better way to open files in Python, it automatically closes the file after the block of code is executed


    # content = file.read() # read the whole file content
    # print("Content of the file:")
    # print(content)


# with open('dummytext.txt', 'w') as file:  # 'w' mode opens the file for writing, truncating the file first
#     file.write("This is a new line added to the file.\n")  # writes a new line to the file
#     file.write("This is another line.\n")   # writes another line to the file
# with open('dummytext.txt', 'a') as file:  # 'a' mode opens the file for appending, keeping the existing content
#     file.write("This line is appended to the file.\n")  # appends a new line to the file
# with open('dummytext.txt', 'r') as file:  # 'r' mode opens the file for reading
#     content = file.read()  # read the whole file content again
#     print("Updated content of the file:")
#     print(content)  # prints the updated content of the file

# with open('dummytext.txt','r') as reader:
#     content = reader.read()  # read the whole file content
#     print("Content of the file:")
#     print(content)

#     content = content.replace("This is a new line added to the file.", "This is a modified line in the file.")  # modify the content
#     print("\nModified content:")
#     print(content)  # prints the modified content

#     reversed_content = content[::-1]  # reverse the content
#     print("\nReversed content:")
#     print(reversed_content)  # prints the reversed content




# with open('dummytext.txt', 'r') as reader:
#     content = reader.read()  # read the whole file content
#     print('content of the file:')
#     print(content)  # prints the content of the file

#     with open('dummytext.txt', 'w') as writer:
#         for line in reversed(content):
#             writer.write(line)  # write the reversed content back to the file
        

with open('dummyText.txt', 'w') as writer:
    writer.write("Hello World, I am writing to a file.\n")  # write a line to the file
    writer.write("This is another line in the file.\n")  # write another line1
    print("File written successfully.")  # print a success message
    writer.close()  # close the file after writing

    with open('dummyText.txt', 'r') as reader:
        content = reader.read()
        print("Content of the file:", content)