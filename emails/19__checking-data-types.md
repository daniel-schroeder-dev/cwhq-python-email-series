## Question

Python is a dynamically typed language, which means a variable can hold any data type during a program's execution. Variables can hold different data types at different points in a program as well. Because of this, it can be difficult to know what data type a value is at any given time in a program.

Consider the case of a function called `add()` which is supposed to add two numbers together and return the result. If we pass two numbers, the function works as expected. But what happens if we pass two strings?

```python
def add(num1, num2):
    return num1 + num2


num_total = add(3, 4)
print(num_total)  # 7

str_total = add("3", "4")
print(str_total)  # '34'
```

Our function will "work" with strings or numbers, but the version with numbers is the expected result. Research how to check the data type of a value in Python and try to fix the `add()` function so that it only performs the `+` operation when both values are integers (you can also check for `float` if you want).

## Answer

```python
def add(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        return "ERROR! Both numbers must be integers!"

    return num1 + num2


num_total = add(3, 4)
print(num_total)  # 7

str_total = add("3", "4")
print(str_total)  # 'ERROR! Both numbers must be integers!'
```

## Explanation

You can use the `isinstance()` function to check if a value has a specific data type (or is a subclass of that data type). The `type()` function can also be used, but it is a bit messier, as the example below shows:

```python
def add(num1, num2):
    if not type(num1) == "<class 'int'>" or not type(num2) == "<class 'int'>":
        return "ERROR! Both numbers must be integers!"

    return num1 + num2


num_total = add(3, 4)
print(num_total)  # 7

str_total = add("3", "4")
print(str_total)  # 'ERROR! Both numbers must be integers!'
```


## Resources

-   [The Python Standard Library Docs - `isinstance()`](https://docs.python.org/3/library/functions.html#isinstance)
