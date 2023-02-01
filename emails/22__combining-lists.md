## Question

A programmer is working on an app that allows users to combine items from multiple shopping carts together. They've got some code written to combine two shopping carts (which are lists) that looks like this:

```python
def combine_shopping_carts(shopping_cart_1, shopping_cart_2):
    combined_carts = shopping_cart_1
    for item in shopping_cart_2:
        combined_carts.append(item)

    return combined_carts

```

Is there a simpler way to write this function in Python?

## Answer

```python
def combine_shopping_carts(shopping_cart_1, shopping_cart_2):
    return shopping_cart_1 + shopping_cart_2

```

## Explanation

In Python, you can use the `+` operator to combine two `lists` into a new list.

## Resources

-   [The Python Tutorial - Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
