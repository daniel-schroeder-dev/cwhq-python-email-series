## Question

A young Pythonista is working on a "Guess The Number" program and wants to tell the user how far off they were if they don't guess correctly, but they don't want to tell them the direction (positive or negative) of their error. They've created a function called `get_absolute_value()` to assist them in this process, and they are testing it out like this before adding it to their program:

```python
def get_absolute_value(number):
    if number < 0:
        number *= -1

    return number

number = -3
absolute_value = get_absolute_value(number)

print(f"The absolute value of {number} is {absolute_value}.")  # The absolute value of -3 is 3.

number = 3
absolute_value = get_absolute_value(number)

print(f"The absolute value of {number} is {absolute_value}.")  # The absolute value of 3 is 3.
```

An experienced Pythonista sees their `get_absolute_value()` function and remarks "You could use a built-in Python function to calculate the absolute value instead of creating your own!". Investigate the many [built-in Python functions](https://docs.python.org/3/library/functions.html) and see if you can find a way to refactor this program to use one instead of the `get_absolute_value()` function. 

## Answer

```python
number = -3
absolute_value = abs(number)

print(f"The absolute value of {number} is {absolute_value}.")  # The absolute value of -3 is 3.

number = 3
absolute_value = abs(number)

print(f"The absolute value of {number} is {absolute_value}.")  # The absolute value of 3 is 3.
```

## Explanation

The `abs()` built-in function returns the absolute value of a number.

## Resources

-   [The Python Docs - `abs()`](https://docs.python.org/3/library/functions.html#abs)
