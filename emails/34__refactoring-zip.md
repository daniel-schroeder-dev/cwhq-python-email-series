## Question

If you've been following this email series, in the last email we talked about the `zip()` function. Our young Pythonista used it to combine a list of `first_names` and `last_names` like this:

```python
first_names = ["Daniel", "Jess", "Bob"]
last_names = ["Smith", "Fury", "Worth"]

full_names = []
for first_name, last_name in zip(first_names, last_names):
    full_names.append((first_name, last_name))
    

print(full_names) # [('Daniel', 'Smith'), ('Jess', 'Fury'), ('Bob', 'Worth')]
```

An older Pythonista sees their approach and is pleased with their program, but notices there's an even more Pythonic way to complete the same task. Research how combining `list()` and `zip()` could completely remove the `for` loop from this program. 

## Answer

```python
first_names = ["Daniel", "Jess", "Bob"]
last_names = ["Smith", "Fury", "Worth"]

full_names = list(zip(first_names, last_names))

print(full_names) # [('Daniel', 'Smith'), ('Jess', 'Fury'), ('Bob', 'Worth')]
```

## Explanation

You can use `zip()` and `list()` to merge items from multiple lists together and store them in a top-level list. 

## Resources

-   [The Python Docs - `zip()`](https://docs.python.org/3/library/functions.html#zip)
