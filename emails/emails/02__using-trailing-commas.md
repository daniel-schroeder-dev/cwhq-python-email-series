## Question

In the code sample below, we've created a `list` representing users of a fictional app:

```python
users = [
    "djs",
    "charlieg",
    "margaret",
    "django"
]
```

Later on, another programmer comes along and decides to add another user to our `users` `list` like so:

```python
users = [
    "djs",
    "charlieg",
    "margaret",
    "django"
    "kavya"
]
```

There's some code in the app that displays all of the users:

```python
for user in users:
    print(user)
```

When the app runs, this is the output:

```text
djs
charlieg
margaret
djangokavya
```

Why is the program displaying "django" and "kavya" as a single `str`? Is there something we could've done to prevent the error that caused those two names to be displayed together?


## Answer and Explanation

Because the original `users` `list` didn't have a trailing comma, it was easy for another programmer to add something to the `users` `list` and forget to put the comma on the old last item.

A better way to write a multi-line `list` would be:

```text
users = [
    "djs",
    "charlieg",
    "margaret",
    "django",   # Trailing comma prevents errors
]
```

