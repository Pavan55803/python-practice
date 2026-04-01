# ============================================================
#                   NUMBER GUESSING GAME
# ============================================================

import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("=" * 40)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 40)
    print("I have picked a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try higher.")
            elif guess > number:
                print("Too high! Try lower.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts!")
                break
        except ValueError:

            print("Please enter a valid number.")
            
number_guessing_game()
