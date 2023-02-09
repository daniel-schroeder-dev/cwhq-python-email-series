## Question

A young Python programmer is building a game where they'll hide treasure inside a 2D gameboard. They are working on the logic to create the gameboard and display the gameboard. Here's what they have so far:

```python
def display_gameboard():
    print(row1)
    print(row2)
    print(row3)


row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]

display_gameboard()
```

*output*
```text
['_', '_', '_']
['_', '_', '_']
['_', '_', '_']
```

There's a lot of repetition here! Also, it's not clear that there's a relationship between each row. The programmer has to understand that they represent three rows of a 2D gameboard. Research how 2D lists work in Python, and see if you can create a better data structure to hold the gameboard. Once you've got the correct data structure, refactor the program to use it in the `display_gameboard()` function.

## Answer

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

## Explanation

2D lists are a handy tool when modeling things like a gameboard. A 2D list is simply a "list of lists".

## Resources

-   [Real Python - Lists Can Be Nested](https://realpython.com/python-lists-tuples/#lists-can-be-nested)
