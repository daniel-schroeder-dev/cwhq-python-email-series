## Question

Python's `dict` data structure stores data in key/value pairs. If you have two `dicts` that you want to combine into a new `dict`, you could do this:

```python
credentials = {
    "username": "djs",
    "password": "myp@$$w3rd",
}

login_status = {
    "is_logged_in": False,
    "login_attempts": 0,
}

user_data = {}

for user_info in [credentials, login_status]:
    for key, value in user_info.items():
        user_data[key] = value

```

It takes 4 lines of code to create a new `dict` from the original `dicts` using the method above. There's a way to do this in a single line though! Research "dictionary unpacking" and see if you can build the `user_data` `dict` in a single line of code.

## Answer

```python
credentials = {
    "username": "djs",
    "password": "myp@$$w3rd",
}

login_status = {
    "is_logged_in": False,
    "login_attempts": 0,
}

# Dictionary unpacking is cool!
user_data = dict(**credentials, **login_status)
```

## Explanation

The `**dict` syntax will unpack the key/value pairs of a `dict` into a function call. The example above is equivalent to:

```python
user_data = dict(username="djs", password="myp@$$w3rd", is_logged_in=False, login_attempts=0)
```

## Resources

-   [Real Python - Unpacking with the Asterisk Operators](https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators)
