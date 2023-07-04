# Number Guessing Game

Welcome to the Number Guessing Game! This is a simple interactive game where you have to guess a randomly generated number within a specified range. Test your guessing skills and see if you can read the computer's mind!

## How to Play

1. Clone the repository or download the script file (`number_guess.py`).
2. Make sure you have Python 3 installed on your system.
3. Run the script by executing the following command in your terminal or command prompt:

   ```bash
   python number_guess.py
Follow the instructions on the screen to set the range of numbers and the number of attempts you want to have.
Enter your guesses within the specified range and try to guess the correct number.
If your guess is too high or too low, the game will provide feedback to help you narrow down your next guess.
Keep guessing until you either guess the correct number or run out of attempts.
After each game, you have the option to play again or exit the game.
Have fun and enjoy the challenge!

## Features
- Customizable range of numbers: You can set the minimum and maximum values for the range within which the random number is generated.
- Adjustable difficulty: You can choose the number of attempts you want to have, making the game easier or harder based on your preference.
- Error handling: The game handles invalid inputs gracefully and provides appropriate error messages to guide the player.
- Play again: You can choose to play the game again after completing a round.

## Example
Here's an example of how the game looks when played:

```bash
Welcome to this Number Guessing Game!
In this number guessing game, you get to determine the range of numbers you want to play with!
You can also adjust the difficulty by choosing the number of attempts you have to guess the number.
Let's see if you can guess the computer's number!

Enter the minimum value of your range: 1
Enter the maximum value of your range: 100
Enter the number of attempts you would like to have: 5

Guess the number: 50
Your guess was too low...
You have 4 attempt(s) remaining.

Guess the number: 75
Your guess was too high...
You have 3 attempt(s) remaining.

Guess the number: 63
Your guess was too high...
You have 2 attempt(s) remaining.

Guess the number: 57
Your guess was too low...
You have 1 attempt(s) remaining.

Guess the number: 60
You did it! You guessed the number!

Do you want to play again? (Y/N): n
```
