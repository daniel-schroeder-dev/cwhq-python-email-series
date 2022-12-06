## Question

In the code sample below, the variable `status` is set to either adult or child depending upon the value of the `age` variable:

```python
age = 18

if age >= 18:
    status = "adult"
else:
    status = "child"
```

Since the body of both conditional statements is only assigning a value to the same variable, you can use a shortcut here and do everything in one line. Research conditional expressions in Python and see if you can figure out how to reduce the conditional statement to a single assignment expression.


## Answer

```python
age = 18

status = "adult" if age >= 18 else "child"
```

## Explanation

Conditional expressions can be used anytime you have a simple `if...else` expression that merely assigns a value to a variable. 

## Resources

-   [Real Python - Conditional Expressions (Python's Ternary Operator)](https://realpython.com/python-conditional-statements/#conditional-expressions-pythons-ternary-operator)
