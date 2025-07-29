# Question18: 01:06:25 - What is the Python “with” statement designed for?
# The Python with statement is designed for resource management and exception handling. It simplifies code that needs to set up and tear down resources — like file handling, database connections, or locks — by automatically managing the setup and cleanup.

# ✅ What it does:
# Ensures that resources are properly released, even if an error occurs.
# Helps prevent resource leaks (e.g., forgetting to close a file).

# 🔁 Without with (manual approach):
file = open("test.txt", "r")
try:
    data = file.read()
finally:
    file.close()  # You must remember to close it

# ✅ With with (recommended):
with open("test.txt", "r") as file:
    data = file.read()
# File is automatically closed after this block
