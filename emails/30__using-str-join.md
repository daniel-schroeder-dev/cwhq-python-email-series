## Question

A Pythonista is working for a popular credit card company and is tasked with taking a list of tuples holding parts of cardholder's names (first, middle, last) and turning it into a list of strings containing the full name.

So, they want to transform this:

```python
[
    ("Carter", "Johnson", "Peters"),
    ("Molly", "Shannon", "Jackson"),
    ("Jerry", "Sandoval", "Smith"),
]
```

Into this:

```python
[
    "Carter Johnson Peters",
    "Molly Shannon Jackson",
    "Jerry Sandoval Smith",
]
```

They've got a working function to perform this task here:

```python
def transform_names(names):
    transformed_names = []

    for name in names:
        full_name = ""
        for name_part in name:
            full_name += name_part + " "

        # Remove the last space
        full_name = full_name.strip()
        transformed_names.append(full_name)

    return transformed_names


names = [
    ("Carter", "Johnson", "Peters"),
    ("Molly", "Shannon", "Jackson"),
    ("Jerry", "Sandoval", "Smith"),
]

transformed_names = transform_names(names)
print(transformed_names)  # ['Carter Johnson Peters', 'Molly Shannon Jackson', 'Jerry Sandoval Smith']
```

A more-experienced developer reviews their code and tells them that they could use `str.join()` to simplify their `transform_names()` function and make this code more Pythonic. Research `str.join()` and see if you can refactor the `transform_names()` function to use this string method.

## Answer

```python
def transform_names(names):
    transformed_names = []

    for name in names:
        full_name = " ".join(name)
        transformed_names.append(full_name)

    return transformed_names


names = [
    ("Carter", "Johnson", "Peters"),
    ("Molly", "Shannon", "Jackson"),
    ("Jerry", "Sandoval", "Smith"),
]

transformed_names = transform_names(names)
print(transformed_names)  # ['Carter Johnson Peters', 'Molly Shannon Jackson', 'Jerry Sandoval Smith']
```

## Explanation

The `str.join()` function allows you to easily pull all items out of a list and create a `str` from those items. Whatever `str` you join the items with will be the separator between each list item (in our case, it was an empty space).

## Resources

-   [Real Python - Going From a List to a String in Python with `.join()`](https://realpython.com/python-string-split-concatenate-join/#going-from-a-list-to-a-string-in-python-with-join)
