## Question

A young Pythonista is working on a program for a local business to pull the unique customer names from a large order history file. There are millions of records in the file, but the programmer is working with a small subset of records (as a list) to get the algorithm for finding unique customer names correct. This is what they have so far:

```python
def get_unique_customers(customers):
    unique_customers = []
    for customer in customers:
        if customer in unique_customers:
            unique_customers.append(customer)

    return unique_customers


customers = ["Bob Smith", "Janice Carencrow", "Jasper Rothchild", "Bob Smith"]
unique_customers = get_unique_customers(customers)

print(unique_customers)  # ['Bob Smith', 'Janice Carencrow', 'Jasper Rothchild']
```

They are happy with their `get_unique_customers()` function as it works correctly. Before they can move on to completing their program, an experienced Pythonista looks over their work and chuckles: "You could use sets to remove the `get_unique_customers()` function entirely!" Investigate how sets work in Python and see if you can refactor this program to use them!

## Answer

```python
customers = ["Bob Smith", "Janice Carencrow", "Jasper Rothchild", "Bob Smith"]
unique_customers = set(customers)

print(unique_customers)  # {'Janice Carencrow', 'Bob Smith', 'Jasper Rothchild'}
```

## Explanation

A set allows you to easily filter duplicate values from a `list`. Note that the data structure of a `set` is not the same as a `list`, but you can easily convert it to a `list` using the `list()` function.

## Resources

-   [The Python Docs - Set Types](https://docs.python.org/3/library/stdtypes.html#types-set)
