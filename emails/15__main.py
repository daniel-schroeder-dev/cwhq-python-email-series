from random import randint

random_number = randint(1, 10)
num_guesses = 1

while True:

    try:
        user_guess = int(input("Guess the number: "))
    except ValueError:
        print("You must enter a valid integer!")
        continue # skips the rest of the loop

    if user_guess == random_number:
        print("That's correct!")
        print(f"It took you {num_guesses} guesses to guess the number.")
        break
    else:
        print("Sorry, that's incorrect. Try again!")
        num_guesses += 1
