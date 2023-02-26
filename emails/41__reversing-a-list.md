## Question

A young Python programmer is working on a program where they need to loop through a list from the last index to the first index and display each item. This is what they've done so far:

```python
users = ["djs", "sahibk", "inder", "django"]

for index in range(len(users) - 1, -1, -1):
    user = users[index]
    print(user)

```

Their program works, but the why they are using `range()` isn't very Pythonic. An older Python programmer tells them to search through Python's built-in functions for a possible solution to reverse the `users` list without using `range()` and `len()`. See if you can help them refactor their program to use a built-in Python function to reverse the list during the loop!

## Answer

```python
users = ["djs", "sahibk", "inder", "django"]

for user in reversed(users):
    print(user)

```

## Explanation

The `reversed()` function allows you to easily loop through a `list` in reverse order.

## Resources

-   [The Python Docs - `reversed()`](https://docs.python.org/3/library/functions.html#reversed)
