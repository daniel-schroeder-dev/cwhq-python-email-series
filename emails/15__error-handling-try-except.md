## Question

Imagine you have a program that asks a user to guess a number until they get it correct, like the one below:

```python
from random import randint

random_number = randint(1, 10)
num_guesses = 0

while True:
    num_guesses += 1

    user_guess = int(input("Guess the number: "))

    if user_guess == random_number:
        print("That's correct!")
        print(f"It took you {num_guesses} guesses to guess the number.")
        break
    else:
        print("Sorry, that's incorrect. Try again!")

```

Say the user accidentally types a non-numeric character, such as the letter "e". Your program in its current state would crash!

```text
Guess the number: 1
Sorry, that's incorrect. Try again!
Guess the number: 2
Sorry, that's incorrect. Try again!
Guess the number: e
Traceback (most recent call last):
  File "/home/daniel/Public/cwhq/python-email-series/emails/15__main.py", line 7, in <module>
    user_guess = int(input("Guess the number: "))
ValueError: invalid literal for int() with base 10: 'e'
```

Notice that a `ValueError` occurs because we're trying to use the `int()` function to create the return value from `input()` to an `int`. If the user supplies something that isn't an `int`, this error crashes our program.

Research `try...except` statements in Python and see if you can create a version of this program that won't crash when an error occurs.

## Answer

```python
from random import randint

random_number = randint(1, 10)
num_guesses = 0

while True:
    num_guesses += 1

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

```

## Explanation

The `try...except` statement allows you to defend against common issues in your program and run some code when they occur. In this case, we were able to prevent the program from crashing and display a message to the user about their error.


## Resources

-   [The Python Tutorial - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
