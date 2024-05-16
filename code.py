import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            # Increment the number of attempts
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print("Congratulations! You've guessed the number ({secret_number}) in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Call the function to start the game
guess_number()
