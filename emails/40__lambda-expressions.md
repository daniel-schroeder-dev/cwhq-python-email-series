## Question

A young Pythonista is trying to sort a list of dictionaries containing items in a shopping cart by their `price` key from low to high. They see that Python has a built-in `sorted` function for this purpose, but they don't understand how to get it to work on a specific key in each dictionary of their `shopping_cart` list, as you can see from the example below:

```python
shopping_cart = [
    {
        "item_name": "XBox 720",
        "price": 799.99,
    },
    {
        "item_name": "Logitech Wireless Mouse",
        "price": 45.75,
    },
    {
        "item_name": "Mechanical Keyboard",
        "price": 245.50,
    },
]

sorted_shopping_cart = sorted(shopping_cart)  # TypeError: '<' not supported between instances of 'dict' and 'dict'

print(sorted_shopping_cart)
```

Research how the `key` parameter of the `sorted()` function works and see if you can fix their program!

## Answer

```python
shopping_cart = [
    {
        "item_name": "XBox 720",
        "price": 799.99,
    },
    {
        "item_name": "Logitech Wireless Mouse",
        "price": 45.75,
    },
    {
        "item_name": "Mechanical Keyboard",
        "price": 245.50,
    },
]

sorted_shopping_cart = sorted(shopping_cart, key=lambda item: item["price"])  

print(sorted_shopping_cart)
```

*output*
```text
[
    {'item_name': 'Logitech Wireless Mouse', 'price': 45.75}, 
    {'item_name': 'Mechanical Keyboard', 'price': 245.5}, 
    {'item_name': 'XBox 720', 'price': 799.99},
]
```

## Explanation

The `key` parameter of the `sorted()` function takes a function as an argument. When you need to do something simple, a lambda function can be used as the value to the `key` parameter. Lambda functions are "anonymous" functions that don't have a name and are usually passed to another function such as how we did with the `sorted()` function.

Here's an example of a named function with the same logic as our lambda function:

```python
def sort_by_price(item):
    return item["price"]


shopping_cart = [
    {
        "item_name": "XBox 720",
        "price": 799.99,
    },
    {
        "item_name": "Logitech Wireless Mouse",
        "price": 45.75,
    },
    {
        "item_name": "Mechanical Keyboard",
        "price": 245.50,
    },
]


sorted_shopping_cart = sorted(shopping_cart, key=sort_by_price)  

print(sorted_shopping_cart)
```

Note that we don't call the `sort_by_price()` function but rather we pass it as an argument. This is possible because functions can be passed around just like other values in Python!

## Resources

-   [Real Python - How to Use Python Lambda Functions](https://realpython.com/python-lambda/)
-   [The Python Docs - `sorted()`](https://docs.python.org/3/library/functions.html#sorted)
