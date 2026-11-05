"""
PS 2 - Number Guessing Game
Language : Python 3
Concepts : Loops, Conditions, Functions, Random
Note     : Player gets 5 attempts. For testing, the secret number
           is fixed to 42 (set TEST_MODE = True below).
"""

import random

# ---------------- Settings ----------------
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 5

# For testing set this to True -> secret number becomes 42
# For the real game keep it False -> secret number is random
TEST_MODE = True
TEST_SECRET = 42


def get_secret_number():
    """Return the secret number (fixed 42 in test mode, else random)."""
    if TEST_MODE:
        return TEST_SECRET
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_guess(attempts_left):
    """Ask the player for a guess until a valid number is entered.
    Invalid input does NOT use up an attempt."""
    while True:
        value = input("Enter your guess (" + str(MIN_NUMBER) + "-"
                      + str(MAX_NUMBER) + "): ").strip()

        # Validate: whole numbers only
        try:
            guess = int(value)
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue

        # Validate: within range
        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print("Out of range. Enter a number between "
                  + str(MIN_NUMBER) + " and " + str(MAX_NUMBER) + ".")
            print("Attempts left: " + str(attempts_left)
                  + " (no attempt lost)")
            continue

        return guess


def play_game():
    """Play one round of the game."""
    secret = get_secret_number()
    attempts_used = 0
    won = False

    print("\nI have picked a number between " + str(MIN_NUMBER)
          + " and " + str(MAX_NUMBER) + ".")
    print("You have " + str(MAX_ATTEMPTS) + " attempts. Good luck!\n")

    while attempts_used < MAX_ATTEMPTS:
        attempts_left = MAX_ATTEMPTS - attempts_used
        guess = get_guess(attempts_left)
        attempts_used += 1
        attempts_left = MAX_ATTEMPTS - attempts_used

        if guess == secret:
            won = True
            break
        elif guess < secret:
            print("Too low! Attempts left: " + str(attempts_left))
        else:
            print("Too high! Attempts left: " + str(attempts_left))

    if won:
        if attempts_used == 1:
            word = "attempt"
        else:
            word = "attempts"
        print("Congratulations! You guessed it in "
              + str(attempts_used) + " " + word + ".")
    else:
        print("Game Over! The number was " + str(secret) + ".")

    print("Attempts used: " + str(attempts_used))


def ask_play_again():
    """Ask 'Play again? (y/n)' until the answer is y or n."""
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        print("Please enter y or n.")


def main():
    print("=== Number Guessing Game ===")
    while True:
        play_game()
        if not ask_play_again():
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()