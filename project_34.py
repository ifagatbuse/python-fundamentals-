# Project 34: Student Registry
# Topic: Store and display student information with OOP

class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}")

students = [
    Student("Alice", 101, "A"),
    Student("Bob", 102, "B"),
    Student("Charlie", 103, "C")
]

print("Student Registry:")
for s in students:
    s.display()
