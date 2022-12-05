## Question

When programming, you often want to check the values stored in variables as you're working on the program. This is especially helpful whenever something isn't working as you expect. 

One way to check the values stored in variables is by printing the variable name and the value stored in the variable:

```python
my_age = 18
print(f"my_age={my_age}")  # my_age=18
```

There's nothing wrong with the above approach, but `f-strings` have a shorthand for this common debugging task. See if you can figure out what this shorthand is by reading through section [2.4.3 Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals) of the Python language reference. 

## Answer

```python
my_age = 18
print(f"{my_age=}")  # my_age=18
```

## Explanation

To display a variable along with the value of the variable, you can simply write the variable name with an `=` next to it inside the `{}`. 

## Resources

-   [The Python Language Docs - 2.4.3 Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)
