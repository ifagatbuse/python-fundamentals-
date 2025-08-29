# Project 17: Number Guessing Game
# Topic: random + input loop + conditions

import random

secret = random.randint(1, 100)  # pick a number between 1 and 100
attempts = 0                      # count how many guesses the user makes

print("I picked a number between 1 and 100. Try to guess it!")

while True:
    guess_text = input("Your guess: ").strip()
    # validate input is an integer
    if not guess_text.isdigit():
        print("Please enter a valid positive integer.")
        continue

    guess = int(guess_text)
    attempts += 1

    # give hints to guide the user
    if guess < secret:
        print("Too low! ")
    elif guess > secret:
        print("Too high! ")
    else:
        print(f"Correct!  The number was {secret}. Attempts: {attempts}")
        break
