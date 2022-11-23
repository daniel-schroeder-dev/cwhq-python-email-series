## Question

Imagine a function called `draw_triangle(height)` that will draw triangles of the given `height` like so:

_main.py_

```python
draw_triangle(4)
draw_triangle(5)
```

_Output_

```text
   ^
  ^^^
 ^^^^^
^^^^^^^
    ^
   ^^^
  ^^^^^
 ^^^^^^^
^^^^^^^^^
```

Below is a definition of the function, but the way to create the `str` for the `blocks` and `spaces` is left blank:

```python
def draw_triangle(height):
    for row_number in range(1, height + 1):
        num_blocks = row_number * 2 - 1
        num_spaces = height - row_number

        blocks = ___  # What goes here?
        spaces = ___  # What goes here?

        row = f"{spaces}{blocks}"
        print(row)


draw_triangle(4)
draw_triangle(5)
```

How could you use the `num_blocks` and `num_spaces` variables to create the `blocks` and `spaces` strings in a single line, without using a loop?

## Answer

```python
def draw_triangle(height):
    for row_number in range(1, height + 1):
        num_blocks = row_number * 2 - 1
        num_spaces = height - row_number

        # String multiplication to the rescue!
        blocks = "^" * num_blocks
        spaces = " " * num_spaces

        row = f"{spaces}{blocks}"
        print(row)


draw_triangle(4)
draw_triangle(5)
```

## Explanation

In Python, you can create copies of a `str` by using the multiplication (`*`) operator.

## Resources

-   [The Python Tutorial - Strings](https://docs.python.org/3/tutorial/introduction.html#strings)
