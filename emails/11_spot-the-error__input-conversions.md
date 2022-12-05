## Question

A student is working on a simple calculator program and has written the following code thus far:

```python
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

total = num1 + num2
print(f"{num1} + {num2} = {total}")
```

When they run the program, the result surprises them though:

```text
Enter the first number: 2
Enter the second number: 3
2 + 3 = 23
```

Where is the bug, and how do we fix it?

## Answer

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

total = num1 + num2
print(f"{num1} + {num2} = {total}")
```

## Explanation

The `input()` function *always* returns a `str`. If you expect the user to type in a number (`int` or `float`) you need to use the appropriate conversion functions `int()` or `float()`. 

## Resources

-   [The CodeWizardsHQ Docs - `int()`](https://docs.codewizardshq.com/python/python-language/#int_1)
