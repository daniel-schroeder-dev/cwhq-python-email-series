## Question

Sometimes, when you want to iterate over a sequence (such as a `str` or a `list`) it can be handy to have a reference to the position of the item (the index number) in the sequence.

A naive we to do this in Python would be something like this:

```python
users = ["Daniel", "Margaret", "Django"]

user_index = 0
for user in users:
    print(f"{user} is at index {user_index}.")
    user_index += 1

```

There's a better way to do this in Python! Research a few of Python's [built-in functions](https://docs.python.org/3/library/functions.html) and see if you can find a better solution. 

## Answer

```python
users = ["Daniel", "Margaret", "Django"]

# Use `enumerate()` to loop through a sequence and get the index numbers.
for user_index, user in enumerate(users):
    print(f"{user} is at index {user_index}.")

```

## Explanation

Python's `enumerate()` function allows you to loop through a sequence and get index number along with the item for each item in the sequence. 

## Resources

-   [The Python Docs - `enumerate()`](https://docs.python.org/3/library/functions.html#enumerate)
