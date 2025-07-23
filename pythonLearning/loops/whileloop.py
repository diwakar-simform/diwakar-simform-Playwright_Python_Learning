# while loop in python is used to execute a block of code repeatedly as long as a given condition is true.
# It is useful when the number of iterations is not known beforehand and depends on a condition being met.
# difference between while and for loop is that while loop = runs until a condition is false, while for loop = runs for a fixed number of iterations or over a sequence.

it = 5

while it > 0:  # condition to check if it is greater than 0
    print("Iteration number: ", it)  # prints the current iteration number
    it -= 1  # decrementing it by 1 in each iteration

it = 5  # resetting it to 5 for the next example
while it > 0:
    if it == 3:
        print("Skipping iteration when it is 3")
    else:
        print("Iteration number: ", it)  # prints the current iteration number
    it -= 1  # decrementing it by 1 in each iteration


print("---------------Example of break statement in while loop------------------")
it = 10  # resetting it to 5 for the next example
while it > 0:
    if it == 5:
        print("Skipping iteration when it is 5")
        it -= 1  # decrement before continue to avoid infinite loop
        continue # skipping the rest of the loop when it is 5
    if it == 3:
        print("Breaking the loop when it is 3")
        break # breaking the loop when it is 3
    else:
        print("Iteration number: ", it)  # prints the current iteration number
    it -= 1  # decrementing it by 1 in each iteration