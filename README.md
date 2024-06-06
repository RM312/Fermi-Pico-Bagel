# Fermi Pico Bagel Game - README

## Overview

The Fermi Pico Bagel game is a fun and engaging number-guessing game where the player attempts to guess a secret number. The game provides feedback on each guess to help the player narrow down the possibilities and ultimately guess the correct number.

## Game Rules

1. **Secret Number**: The game starts with a predefined secret number (e.g., '5489').
2. **Guessing**: The player guesses a number with the same number of digits as the secret number.
3. **Feedback**:
   - **Fermi**: A digit is correct and in the correct position.
   - **Pico**: A digit is correct but in the wrong position.
   - **Bagels**: No digits are correct.

## How to Play

1. **Start the Game**: The game begins with a predefined secret number, which the player needs to guess.
2. **Input a Guess**:
   - The guess must have the same number of digits as the secret number.
   - The guess must not contain duplicate digits.
3. **Receive Feedback**:
   - If the guess matches the secret number exactly, the player wins, and the game ends with a congratulatory message.
   - If not, the game provides feedback:
     - **Fermi** for each correct digit in the correct position.
     - **Pico** for each correct digit in the wrong position.
     - **Bagels** if no digits are correct.
4. **Continue Guessing**: The player continues to guess based on the feedback until the correct number is guessed.

## Example Gameplay

1. **Secret Number**: 5489
2. **Player Guess**: 1234
   - Feedback: Bagels (none of the digits match the secret number)
3. **Player Guess**: 5678
   - Feedback: Pico Pico (digits 5 and 8 are correct but in the wrong positions)
4. **Player Guess**: 5489
   - Feedback: Fermi Fermi Fermi Fermi (all digits are correct and in the correct positions)
   - The player wins the game!

## Error Handling

- If the player enters a guess with a different number of digits than the secret number, the game prompts the player

to enter a guess with the correct number of digits.
- If the player enters a guess with duplicate digits, the game informs the player of the error and prompts for a new guess.

## Winning the Game

The game continues until the player guesses the secret number correctly. When the correct number is guessed, the game displays a congratulatory message indicating that the player has won.

## Notes

- The secret number in this game is hard-coded as '5489', but you can modify this to any other number of your choice by changing the `original_number` variable in the code.
- Ensure that the secret number and all guesses follow the rules of having unique digits and matching the length of the secret number.

## Customization

To customize the game, you can:
- Change the `original_number` to a different value.
- Modify the feedback messages for a more personalized experience.
- Adjust the rules for the game if desired (e.g., allowing guesses with duplicate digits).

Enjoy playing the Fermi Pico Bagel game and challenge your friends to see who can guess the number fastest!
