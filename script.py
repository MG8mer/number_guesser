import random

print("Welcome to this Number Guessing Game!")
print("")
print("Your objective is to guess a randomly generated number from 1 to 100!")
print("The caveat, however, is that you must do this within 10 attempts!")
print("")
print("Can you read the computer's mind and succeed this challenge? We shall find out...")
print("")

def number_guess():
    guess = None
    attempts = 0

    while True:
        if attempts == 10:
            print("Game over! You've exhausted your attempts.")
            print("")
            print(f"The number was {rng_game}.")
            response = input("Wanna do it again? Y/N: ")
            print("")
            if response == 'Y' or response == 'y':
                attempts = 0
            else:
                break
        if attempts == 0:
            rng_game = random.randint(1, 100)
        while guess is None:
                try:
                    guess = int(input("Guess the number: "))
                except ValueError:
                    print(f"That wasn't an integer... Your guess must be an integer between 1 and 100. Don't worry, you still have {10 - attempts} attempts remaining.")
                    print("")
        if attempts == 10 and response != 'Y' and response != 'y':
            break

        if guess > rng_game:
            if guess > 100:
                print(f"That guess is higher than 100!... Remember, your guess must be between 1 and 100. Don't worry, you still have {10 - attempts} attempts remaining.")
                print("")
                guess = None
            else:
                attempts += 1
                print(f"Your guess was too high... You have {10 - attempts} attempts remaining.")
                print("")
                guess = None
        elif guess < rng_game:
            if guess < 1:
                print(f"That guess is lower than 1!... Remember, your guess must be between 1 and 100. Don't worry, you still have {10 - attempts} attempts remaining.")
                print("")
                guess = None
            else:
                attempts += 1
                print(f"Your guess was too low... You have {10 - attempts} attempts remaining.")
                print("")
                guess = None
        elif guess == rng_game:
            print("You did it! You're a natural!!")
            print("")
            guess = None
            response = input("Wanna do it again? Y/N: ")
            print("")
            if response == 'Y' or response == 'y':
                attempts = 0
            else:
                break

number_guess()
