# 1. - Student class with attributes

class Student:
    def __init__(self, name, age, grade):
        self.name = name      # instance variable
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# student1 = Student("Ravi", 16, "10th")
students = []

def add_student(name, age, grade):
    students.append(Student(name, age, grade))

add_student("Ravi", 16, "10th")
add_student("Sita", 15, "9th")
add_student("Rahul", 17, "11th")

for student in students:
    student.display_info()

# 2. - Read/write to a file

# Writing
with open("students.txt", "w") as file:
    for student in students:
        file.write(f"{student.name},{student.age},{student.grade}\n")

# Reading
with open("students.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# 3. - To-do list mini app

tasks = []

def add_task(task):
    tasks.append(task)
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def view_tasks():
    with open("tasks.txt", "r") as file:
        print("To-Do List:")
        for line in file:
            print("-", line.strip())

add_task("Buy groceries")
add_task("Study Python")
add_task("After finishing python learn -> start learning playwright")
view_tasks()
