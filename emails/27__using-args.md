## Question

A Pythonista is working on a calculator program. They want users to be able to add 2, 3, or 4 numbers together at once. They've created three functions to perform this task:

```python
def add2(num1, num2):
    total = num1 + num2
    return total


def add3(num1, num2, num3):
    total = num1 + num2 + num3
    return total


def add4(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    return total


total = add2(3, 4)
print(total)  # 7

total = add3(3, 4, 2)
print(total)  # 9

total = add4(3, 4, 2, 5)
print(total)  # 14
```

Is there a way to create a single `add()` function instead of three separate ones? Research Python's `*args` syntax for a possible solution!

## Answer

```python
def add(*nums):
    total = sum(nums)
    return total


total = add(3, 4)
print(total)  # 7

total = add(3, 4, 2)
print(total)  # 9

total = add(3, 4, 2, 5)
print(total)  # 14
```

## Explanation

If you define a parameter with a `*` in front of it, that means it will aggregate (group together) all of the arguments passed to a function into a tuple. In our example, `nums` will be a tuple containing all arguments passed to the `add()` function. We can then use the `sum()` built-in function to sum all of the numbers at once.

## Resources

-   [Real Python - kwargs and args](https://realpython.com/python-kwargs-and-args/)
-   [The Python Docs - `sum()`](https://docs.python.org/3/library/functions.html#sum)
