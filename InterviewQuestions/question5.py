# Question5: 15:16 - How do you read and write files in Python?

with open('test.txt', 'a') as f:
    f.write("Hello world !!\n")

with open('test.txt', 'r') as f:
    content = f.read()
    print("File content = ", content)



# 🔑 File Open Modes in Python
# Mode	Meaning	Effect
# 'r'	Read (default)	Opens file for reading (error if file doesn't exist).
# 'w'	Write	Opens file for writing (creates file if not exist, truncates if it does).
# 'a'	Append	Opens file to append content (creates file if not exist, keeps existing content).
# 'x'	Create	Creates a new file and raises error if file already exists.
# 'r+'	Read & Write	Opens file for both reading and writing. File must exist.
# 'w+'	Write & Read	Truncates file to zero length or creates a new file for read/write.
# 'a+'	Append & Read	Opens file for both appending and reading (no truncation).
