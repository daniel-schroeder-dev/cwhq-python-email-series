## Question

Imagine we have a function called `sum_prices()` that takes a `list` called `prices` as a parameter and displays the sum of all the prices in the list.


```python
def sum_prices(prices):
    num_prices = len(prices)
    if num_prices < 2:
        print(f"You passed {num_prices} price(s) but must pass at least 2!")
        return

    prices_sum = sum(prices)
    print(f"The sum of the prices is ${prices_sum}.")

```

We're only using `num_prices` as part of the conditional statement (a guard condition) that ensures we have more than one price to sum, so it's a bit annoying to have to create a variable in the top-level of the function to hold this value, right? 

Python's "walrus" operator was added to the language (in Python 3.8 and above) to deal with this issue! Research how it works and use it to refactor the above example.

## Answer

```python
def sum_prices(prices):
    if (num_prices := len(prices)) < 2:
        print(f"You passed {num_prices} price(s) but must pass at least 2!")
        return

    prices_sum = sum(prices)
    print(f"The sum of the prices is ${prices_sum}.")

```

## Explanation

The "walrus" operator allows us to assign a value to a variable (`num_prices` in this case) while also using the value in an expression (we check if it is less than 2). Note that the parentheses around the expression are required in this example. If you leave them off, the value of the comparison `len(prices) < 2` will be stored in `num_prices`, which isn't what you want!


## Resources

-   [RealPython.com - The Walrus Operator](https://realpython.com/python-walrus-operator/#:~:text=Starting%20in%20early%202019%2C%20Python,alpha%20release%20of%20Python%203.8.)
