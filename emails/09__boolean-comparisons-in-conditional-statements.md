## Question

Whenever you're comparing a value in a conditional statement, the result is a `bool`. If you are testing an unknown value and want to know if it is `True` or `False`, one way is to use `==` between the unknown values and a `bool`, as in the example below:

```python
if is_admin == True:
    print("Welcome, admin!")
else:
    print("Welcome, user!")
```

Is there another way to write the above conditional statement that doesn't need the `==` comparison with a `bool`?

## Answer

```python
if is_admin:
    print("Welcome, admin!")
else:
    print("Welcome, user!")
```

## Explanation

If you are testing for a `bool` value in a conditional statement, you don't need to compare the unknown value with a `bool`. All the conditional expression needs is a `bool` value, and if the unknown value has to be a `bool` already, the additional `==` comparison isn't needed.

## Resources

-   [The CodeWizardsHQ Docs - Conditional Statements](https://docs.codewizardshq.com/python/python-language/#conditional-statements)
