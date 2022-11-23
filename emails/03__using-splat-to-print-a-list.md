## Question

When given the `list` of `favorite_foods` shown below, how could you display each item in the `list` on separate lines using a single `print()` statement and no loops?

```python
favorite_foods = [
    "nachos",
    "sushi",
    "tacos",
]
```

## Answer

```python
favorite_foods = [
    "nachos",
    "sushi",
    "tacos",
]

print(*favorite_foods, sep="\n")
```

## Explanation

The _splat_ operator (`*`) unpacks all of the items in a sequence and passes them to the function. The `sep` argument adds a separator of your choosing between each argument to `print()`. You could write the above statement like this without the _splat_ operator:

```python
favorite_foods = [
    "nachos",
    "sushi",
    "tacos",
]

print(favorite_foods[0], favorite_foods[1], favorite_foods[2], sep="\n")
```

## Resources

-   [Asterisks in Python - Trey Hunner](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/#Asterisks_for_unpacking_into_function_call)
