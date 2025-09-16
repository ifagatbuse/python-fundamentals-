# Project 30: Hangman Game
# Topic: Word guessing game

import random

words = ["python", "computer", "science", "programming", "keyboard"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6

print("Welcome to Hangman!")

while tries > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i, ch in enumerate(word):
            if ch == guess:
                guessed[i] = ch
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

if "_" not in guessed:
    print("You won! Word was:", word)
else:
    print("Game over! Word was:", word)
