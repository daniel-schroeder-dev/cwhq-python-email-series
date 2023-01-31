## Question

When using the `input()` function, a `str` is __always__ returned. This means you need to convert the return value of `input()` to one of the common numeric data types (`int` or `float`) if you want to use the returned value in a mathematical expression.

```python
user_integer = input("Enter an integer: ")
user_float = input("Enter a decimal number: ")

# Neither of these are numbers!
print(type(user_integer))  # <class 'str'>
print(type(user_float))    # <class 'str'>
```

Fix the example above by converting the `user_integer` to an `int` and the `user_float` to a `float`.

## Answer

```python
user_integer = int(input("Enter an integer: "))
user_float = float(input("Enter a decimal number: "))

# Both are now numbers!
print(type(user_integer))  # <class 'int'>
print(type(user_float))    # <class 'float'>
```

## Explanation

You can use the `int()` and `float()` functions to convert data to those data types. There are other conversion functions such as `str()` for creating data to a `str` that come in handy when writing Python programs.

## Resources

-   [Real Python - How to Convert a Python String to int](https://realpython.com/convert-python-string-to-int/)
-   [The Python Standard Library Docs - `float()`](https://docs.python.org/3/library/functions.html#float)
