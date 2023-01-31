## Question

The code sample below ensures that the `denominator` parameter is not `0` before performing the division operation.

```python
def divide(numerator, denominator):
    if denominator == 0:
        print("The denominator must not be 0!")
    else:
        quotient = numerator / denominator
        print(f"{numerator} / {denominator} = {quotient}")


```

Is there a way to still print both messages (error and success) but not use an `else` clause in this function definition?

## Answer

```python
def divide(numerator, denominator):
    if denominator == 0:
        print("The denominator must not be 0!")
        return

    quotient = numerator / denominator
    print(f"{numerator} / {denominator} = {quotient}")

```

## Explanation

You can use an empty `return` statement to exit a function. The pattern shown above (where we exit a function if a parameter holds an invalid value) is often called a __Guard Condition__, and early `return` statements are one way to allow a Guard Condition to protect a function from bad data.

