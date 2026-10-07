# Guess the Number
# The computer picks a secret number, and you try to guess it.

import random  # lets us use Python's built-in "random" tools

secret = random.randint(1, 100)  # pick a random whole number from 1 to 100
guesses = 0                      # count how many tries you've taken

print("I'm thinking of a number between 1 and 100.")

while True:  # keep repeating until we say "break"
    guess = int(input("Your guess: "))  # int = a whole number
    guesses = guesses + 1

    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print("You got it in", guesses, "guesses!")
        break  # stop repeating, the game is over
