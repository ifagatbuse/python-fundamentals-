# Project 18: Rock–Paper–Scissors
# Topic: random + input + conditions

import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock–Paper–Scissors!")
print("Type rock, paper, or scissors (or 'quit' to stop).")

while True:
    user = input("Your choice: ").lower().strip()
    
    if user == "quit":
        print("Game over. Thanks for playing! 👋")
        break
    
    if user not in options:
        print("Invalid choice, try again!")
        continue
    
    computer = random.choice(options)
    print("Computer chose:", computer)
    
    if user == computer:
        print("It's a tie! 🤝")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win! 🎉")
    else:
        print("You lose! 😢")
