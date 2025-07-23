#  1. Multiplication Table (e.g. for 5)

tableOf = int(input("Please enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    print(f"{tableOf} x {i} = {tableOf * i}")

    # print (tableOf, "x", i, "=", tableOf * i) # another way to print the multiplication table

# 2. Star Pattern: Right-angled triangle:

rows = int(input("Please enter the number of rows for the star pattern: "))

for i in range(1, rows+1):
    for j in range(i):
        print("*", end = "") 
        #end="" tells Python not to go to the next line after printing — it ends the print statement with an empty string instead of a newline.
        # is it necessary to use end=""? Yes, it is necessary if you want to print all stars in the same line without spaces.

    print()  # Move to the next line after each row

for i in range(1, rows+1):
    print("*"*i) # Print * i times on the same line.

# 3. Number pattern:
rowNum = int(input("Please enter the number of rows for the number pattern: "))
for i in range(1, rowNum+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 4. sum of even odd numbers from 1 to n
n = int(input("Please enter the number up to which you want to calculate the sum of even and odd numbers: "))

even_sum = 0
odd_sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"sum of even numbers from 1 to {n} is: {even_sum}")
print(f"sum of odd numbers from 1 to {n} is: {odd_sum}")


