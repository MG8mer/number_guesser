import random

def number_guess():
    print("Welcome to this Number Guessing Game!")
    print("In this number guessing game, you get to determine the range of numbers you want to play with!")
    print("You can also adjust the difficulty by choosing the number of attempts you have to guess the number.")
    print("Let's see if you can guess the computer's number!")

    while True:
        x, y, z = get_range_and_attempts()
        rng_game = random.randint(x, y)
        attempts = 0

        while attempts < z:
            guess = get_guess(x, y, attempts, z)
            if guess is None:
                continue

            if guess < rng_game:
                print("Your guess was too low...")
            elif guess > rng_game:
                print("Your guess was too high...")
            else:
                print("You did it! You guessed the number!")
                break

            attempts += 1
            print(f"You have {z - attempts} attempt(s) remaining.")

        if attempts == z:
            print(f"Game over! You've exhausted your attempts. The number was {rng_game}.")

        response = input("Do you want to play again? (Y/N): ")
        if response.lower() != 'y':
            break

        print()

def get_range_and_attempts():
    while True:
        try:
            x = int(input("Enter the minimum value of your range: "))
            y = int(input("Enter the maximum value of your range: "))
            z = int(input("Enter the number of attempts you would like to have: "))

            if x >= y:
                print("Invalid range! The minimum value should be smaller than the maximum value.")
            elif z <= 0:
                print("Invalid number of attempts! You must have at least 1 attempt.")
            else:
                return x, y, z

        except ValueError:
            print("Invalid input! Please enter integers for range and attempts.")

def get_guess(x, y, attempts, max_attempts):
    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess < x or guess > y:
                print(f"Your guess should be between {x} and {y}.")
            else:
                return guess

        except ValueError:
            print("Invalid input! Please enter an integer.")

        attempts += 1
        print(f"Don't worry, you still have {max_attempts - attempts} attempt(s) remaining.")

    return None

number_guess()
