# Bhavesh-Verma
Python Project
# Number Guessing Game (PS 2)

**University:** Rungta International Skills University
**School:** School of Information Technology
**Course:** Bachelor of Computer Application (BCA)
**Language:** Python 3
**Concepts:** Loops, Conditions, Functions, Random

## Problem Statement

Create a game in which the computer picks a random number between 1 and 100 and the player guesses it within limited attempts, receiving "Too high" or "Too low" hints.

**Note:** Player gets 5 attempts. For testing, the secret number is fixed to 42.

## Features

- Secret number generated using the `random` module
- Player gets 5 attempts with "Too high" / "Too low" hints
- Input validation (whole numbers only, within range 1 to 100)
- Invalid input does not use up an attempt
- Shows attempts used at the end of each game
- Asks "Play again? (y/n)" after every game

## Project Structure

```
number_guessing_game.py   # complete solution (single file)
README.md                 # documentation
```

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

```
python number_guessing_game.py
```

### Test Mode

For testing, open `number_guessing_game.py` and change this line:

```
TEST_MODE = False
```

to

```
TEST_MODE = True
```

The secret number will then always be 42. Set it back to `False` to play with a random number.

## How It Works

| Function | Purpose |
|---|---|
| `get_secret_number()` | Returns 42 in test mode, else a random number from 1 to 100 |
| `get_guess()` | Reads and validates the player's guess (number, in range) |
| `play_game()` | Runs one round using a loop for 5 attempts |
| `ask_play_again()` | Asks "Play again? (y/n)" and validates the answer |
| `main()` | Runs the game repeatedly until the player says no |

## Test Cases (secret number = 42)

| # | Scenario | Input | Expected Output |
|---|---|---|---|
| 1 | Normal input | Guess: 42 | Congratulations! You guessed it in 1 attempt. |
| 2 | Boundary / minimum | Guesses: 1, then 100 | Too low! Attempts left: 4 \| Too high! Attempts left: 3 |
| 3 | Invalid input | Guesses: abc, then 150 | Invalid input. Enter a whole number. \| Out of range. Enter a number between 1 and 100. Attempts left: 5 (no attempt lost) |
| 4 | Different valid scenario | Guesses: 10, 90, 50, 30, 20 | Too low \| Too high \| Too high \| Too low \| Too low, then Game Over! The number was 42. |

All 4 test cases pass.

## Author

Name: _your name here_
Enrollment No.: _your enrollment number here_
