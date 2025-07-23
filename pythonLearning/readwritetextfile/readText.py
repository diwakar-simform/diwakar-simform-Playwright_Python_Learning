file = open('dummytext.txt') 
# print(file.read()) # this read method reads the whole file and returns it as a string
# NOTE: You can not have multiple read() calls without seeking to the beginning of the file again, as the cursor will be at the end of the file after the first read.

# print(file.read(3)) # file.read(10) # reads the first 10 characters of the file

# file.readline() # reads the first line of the file
# file.readlines() # reads the whole file and returns it as a list of lines
# file.seek(0) # moves the cursor to the beginning of the file, so you can read it again
# file.tell() # returns the current position of the cursor in the file

# len(file.readlines()) # returns the number of lines in the file
# reading content line by line using loop.
# for i in range(0, 6):
#     print(i+1, "Line: ", file.readline())

# print(file.readlines())

# line = file.readline()
#
# while line != "":
#     print("Line: ",line)
#     line = file.readline()
#

# line = file.readlines()

# print(line)

# # lineCount = len(line) # returns the number of lines in the file

# lineCount = 0

# print("Total number of lines in the file: ", lineCount)
# print()

# for i in line:
#     lineCount += 1
#     print(lineCount, "Line: ",i)

for line in file.readlines():
    print(line.strip())  # .strip() removes the newline character at the end of each line

file.close() # anytime you open file make sure closing it. if not > there will be memory leaks