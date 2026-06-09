
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python to practice string manipulation, loops, conditionals, and user interaction while implementing game logic and win/lose conditions.

## 📝 Tasks

### 🛠️ Hangman Game Core

#### Description
Implement the main Hangman game loop so the player can guess letters, see progress, and know how many incorrect attempts remain.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Ask the player to guess one letter at a time.
- Display the current word progress using underscores for hidden letters, such as `_ _ a _ _`.
- Track and show the number of incorrect guesses remaining.
- End the game when the player guesses the full word or runs out of attempts.

### 🛠️ Game Feedback and Validation

#### Description
Add user-friendly feedback and input validation so the game responds correctly to repeated guesses and invalid input.

#### Requirements
Completed program should:

- Inform the player when a guessed letter is correct or incorrect.
- Prevent duplicate guesses from counting against the player.
- Handle invalid input gracefully (for example, non-letter input or more than one character).
- Display a final message for a win or a loss.

