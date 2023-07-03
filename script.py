import random

print("Welcome to this Number Guessing Game!")
print("")
print("In this number guessing game, you get to determine the range of numbers you want your run to have!")
print("You also are able to alter the difficulty by determining the amount of attempts you have to guess said number!")
print("")
print("Will you be able to read the computer's mind and succeed this challenge? We shall find out...")
print("")

def number_guess():
    guess = None
    attempts = 0
    invalid_attempts = 0

    x = None
    y = None
    z = None

    while True:
        if attempts == z:
            print("Game over! You've exhausted your attempts.")
            print("")
            print(f"The number was {rng_game}.")
            response = input("Wanna do it again? Y/N: ")
            print("")
            if response == 'Y' or response == 'y':
                attempts = 0
                invalid_attempts = 0
                x = None
                y = None
                z = None
            else:
                break
        if x == None and y == None and z == None:
            while True:
                while True:
                    try:
                        x = int(input("Input the minimum value of your range: "))
                    except ValueError:
                        print("That wasn't an integer... Please try again.")
                        print("")
                    try:
                        y = int(input("Input the maximum value of your range: "))
                    except ValueError:
                        print("That wasn't an integer... Please try again.")
                        print("")
                    while True:
                        if x > y:
                            print("")
                            print("Your minimum value is larger than your maximum... Try again.")
                            print("")
                            break
                        if x == y:
                            print("")
                            print("Your minimum value is equal to your maximum... Try again.")
                            print("")
                            break
                        elif x < y:
                            break
                    if x < y:
                        break
                while True:
                    try:
                        z = int(input("Input the amount of attempts you would like to have: "))
                    except ValueError:
                        print("That wasn't an integer... Please try again.")
                        print("")
                    while True:
                        if z <= 0:
                            print("")
                            print("You can't have less than 1 attempt... Try again.")
                            print("")
                            break
                        elif z > 0:
                            break
                    if z > 0:
                        break
                while True:
                    print("")
                    print(f"Scenario: You're guessing a random number from {x} to {y} and you have {z} attempt(s) to do so.")
                    print("")
                    redo = input("Would you like to reset your scenario? Y/N: ")
                    if redo == "N" or redo == "n":
                        print("")
                        print("Good luck!")
                        print("")
                        break
                    else:
                        print("")
                        break
                if redo == "N" or redo == "n":
                    break

        if attempts == 0 and invalid_attempts == 0:
            rng_game = random.randint(x, y)
        while guess is None:
                try:
                    guess = int(input("Guess the number: "))
                except ValueError:
                    invalid_attempts += 1
                    print(f"That wasn't an integer... Your guess must be an integer between 1 and 100. Don't worry, you still have {z - attempts} attempts remaining.")
                    print("")
        if attempts == z and response != 'Y' and response != 'y':
            break

        if guess > rng_game:
            if guess > y:
                invalid_attempts += 1
                print(f"That guess is higher than {y}!... Remember, your guess must be between {x} and {y}. Don't worry, you still have {z - attempts} attempts remaining.")
                print("")
                guess = None
            else:
                attempts += 1
                print(f"Your guess was too high... You have {z - attempts} attempts remaining.")
                print("")
                guess = None
        elif guess < rng_game:
            if guess < x:
                invalid_attempts += 1
                print(f"That guess is lower than {x}!... Remember, your guess must be between {x} and {y}. Don't worry, you still have {z - attempts} attempts remaining.")
                print("")
                guess = None
            else:
                attempts += 1
                print(f"Your guess was too low... You have {z - attempts} attempts remaining.")
                print("")
                guess = None
        elif guess == rng_game:
            print("You did it! You're a natural!!")
            print("")
            guess = None
            response = input("Wanna do it again? Y/N: ")
            print("")
            invalid_attempts = 0
            x = None
            y = None
            z = None
            if response == 'Y' or response == 'y':
                attempts = 0
            else:
                break
number_guess()
