## Question

A young Pythonista is learning about 2D lists, and recently created this portion of a program that'll have a 2D gameboard:

```python
def display_gameboard():
    for row in gameboard:
        print(row)


row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]

gameboard = [row1, row2, row3]

display_gameboard()
```

*output*
```text
['_', '_', '_']
['_', '_', '_']
['_', '_', '_']
```

A more experienced programmer tells them that they could build the `gameboard` using list multiplication in a single line. They also tell them they could display the `gameboard` without using a loop if they used the `*` operator and `sep` parameters of the `print()` function. Research these concepts and see if you can apply them to refactoring this program.


## Answer

```python
def display_gameboard():
    print(*gameboard, sep="\n")


gameboard = [["_"] * 3] * 3
display_gameboard()
```

## Explanation

You can use the `*` operator to create lists of any size containing the same element(s). Here, we use it to build a 2D list (3 inner lists, each containing 3 items). If you've followed this series so far, you'll remember that you can pass multiple arguments to `print()` using the `*` operator and that you can change the separator between those items (a newline in our case) using the `sep` parameter.


## Resources

-   [The Python Docs - Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
-   [The Python Docs - `print()`](https://docs.python.org/3/library/functions.html#print)
