## Question

In the function below, a `bool` value is returned based on the value of the `user_balance` variable: 

```python
def has_balance_remaining(username):
    user_balance = get_user_balance(username)
    if user_balance > 0:
        return True
    else:
        return False
```

Is there a way to write this function without the conditional statement and explicit `bool` `return` statements?

## Answer

```python
def has_balance_remaining(username):
    user_balance = get_user_balance(username)
    return user_balance > 0
```

## Explanation

Since the statement `user_balance > 0` returns a `bool` value, we can simply return the result of that expression instead of using a conditional statement with multiple `return` statements.

