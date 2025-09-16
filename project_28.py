# Project 28: Random Story Generator
# Topic: Generate funny random stories

import random

names = ["Alice", "Bob", "Charlie", "Diana"]
places = ["New York", "Paris", "Tokyo", "Berlin"]
activities = ["found a treasure", "fought a dragon", "won a lottery", "discovered a secret"]

story = f"{random.choice(names)} in {random.choice(places)} {random.choice(activities)}."
print("Random Story:", story)
