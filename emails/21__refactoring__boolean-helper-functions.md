## Question

Readability is important when writing programs. While programs are executed by a computer, they are read by humans. With that in mind, can you think of a way to use functions to make this code more readable?

```python
from random import randint

random_number = randint(1, 10)

if random_number % 2 == 0:
    print("You got a point!")
    score += 1
else:
    print("Sorry, no points for you!")

```

## Answer

```python
from random import randint

# This is a boolean helper function. It takes a condition from
# a conditional statement and gives it a name.
def is_even(number):
    return number % 2 == 0


random_number = randint(1, 10)

# It's really easy to understand how a user gets a point now!
if is_even(random_number):
    print("You got a point!")
    score += 1
else:
    print("Sorry, no points for you!")

```

## Explanation

If you have complex logic in a conditional statement, you can create a function that holds the conditional expression and returns the result. This way, you can give a name to the conditional expression. In our example, the original expression may have been a bit hard to understand at a glance for someone reading your code (or for you a few months after writing it). By creating a function called `is_even()`, it's really easy to understand what the conditional expression is checking.

