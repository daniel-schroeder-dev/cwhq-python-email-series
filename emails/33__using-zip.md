## Question

A young Python programmer is working on a program to combine a list of first names and last names into a single list. This is what they have so far:

```python
first_names = ["Daniel", "Jess", "Bob"]
last_names = ["Smith", "Fury", "Worth"]

full_names = []
for index, first_name in enumerate(first_names):
    last_name = last_names[index]
    full_names.append((first_name, last_name))
    

print(full_names) # [('Daniel', 'Smith'), ('Jess', 'Fury'), ('Bob', 'Worth')]
```

They are pretty happy with the fact that they used `enumerate()`, but an experienced Python programmer tells them there's an even better way to do this using a built-in function called `zip()`. Research this function and see if you can find a simpler way to perform this loop!

## Answer

```python
first_names = ["Daniel", "Jess", "Bob"]
last_names = ["Smith", "Fury", "Worth"]

full_names = []
for first_name, last_name in zip(first_names, last_names):
    full_names.append((first_name, last_name))
    

print(full_names) # [('Daniel', 'Smith'), ('Jess', 'Fury'), ('Bob', 'Worth')]
```

## Explanation

The `zip()` function allows you to loop through two sequences at once. The sequences should both be of the same length. 

## Resources

-   [The Python Docs - `zip()`](https://docs.python.org/3/library/functions.html#zip)
