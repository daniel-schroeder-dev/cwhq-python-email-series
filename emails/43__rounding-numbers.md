## Question

A young Pythonista is working on a program that will implement the "Banker's Rounding" algorithm to round numbers in the form x.x to the nearest integer. The algorithm is as follows:

```text
If the number is equidistant from the two nearest integers (i.e., ends in .5), round to the nearest even integer.
    - So, 1.5 rounds up to 2, and 2.5 rounds down to 2.
All other numbers round to the nearest integer.
    - So, 1.1 to 1.4 round down to 1, while 1.6 to 1.9 round up to 2.
```

Here is their attempt at building a `bankers_round()` function so far:

```python
def bankers_round(number):
    rounded_number = None
    # Gives a rounded down integer of the number
    rounded_down_number = int(number)
    fractional_part = number - rounded_down_number

    if fractional_part > 0.5:
        rounded_number = rounded_down_number + 1
    elif fractional_part < 0.5:
        rounded_number = rounded_down_number
    # Banker's round takes effect
    elif fractional_part == 0.5:
        # If the rounded down number is even
        if rounded_down_number % 2 == 0:
            rounded_number = rounded_down_number
        else:
            rounded_number = rounded_down_number + 1

    return rounded_number



print(bankers_round(1.1))  # 1
print(bankers_round(1.5))  # 2
print(bankers_round(1.6))  # 2

print(bankers_round(2.1))  # 2
print(bankers_round(2.5))  # 2
print(bankers_round(2.6))  # 3
```

Their algorithm works perfectly! They show this to a more experienced Pythonista who shakes their head and says: "You did well, but Python has a built-in function that will perform this task for you!" Investigate the Python's [built-in functions](https://docs.python.org/3/library/functions.html) and see if you can find a way to replace `bankers_round()` with one of them!

## Answer

```python
print(round(1.1))  # 1
print(round(1.5))  # 2
print(round(1.6))  # 2

print(round(2.1))  # 2
print(round(2.5))  # 2
print(round(2.6))  # 3
```

## Explanation

The built-in `round()` function implements the Banker's Rounding algorithm already, so there's no need to create your own version!

## Resources

-   [The Python Docs - `round()`](https://docs.python.org/3/library/functions.html#round)
