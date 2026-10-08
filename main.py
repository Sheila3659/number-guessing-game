import random

def play():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            return

    print(f"Game over! The number was {secret}.")

play()