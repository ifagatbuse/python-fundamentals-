# Project 32: Person Class (OOP Intro)
# Topic: Introduction to Object-Oriented Programming (OOP)

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Hi, I’m {self.name}, {self.age} years old from {self.city}.")

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}, you are now {self.age}!")

p1 = Person("Alice", 20, "New York")
p2 = Person("Bob", 25, "London")

p1.introduce()
p2.introduce()
p1.have_birthday()
