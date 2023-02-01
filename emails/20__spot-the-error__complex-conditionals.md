## Question

In the following code sample, the programmer is trying to determine if a user is the appropriate age to sign up for a service. For this particular service, users must be between the ages of 8 and 12 (inclusive). For some reason, users of any age can sign up, though! Can you spot the error?

```python
user_age = int(input("How older are you? "))

if user_age >= 8 or user_age <= 12:
    print("You can sign up for our service!")
else:
    print("Sorry, you must be between the ages of 8 and 12 (inclusive) to sign up for our service.")

```

## Answer

```python
user_age = int(input("How older are you? "))

# You have to use `and` here!
if user_age >= 8 and user_age <= 12:
    print("You can sign up for our service!")
else:
    print("Sorry, you must be between the ages of 8 and 12 (inclusive) to sign up for our service.")

```

## Explanation

The `or` operator will return `True` if _either_ condition is `True`. When trying to check a range, we need to use the `and` operator, as it ensures that _both_ conditions are `True` before returning `True`.

## Resources

-   [The CodeWizardsHQ Docs - Logical Operators](https://docs.codewizardshq.com/python/python-language/#logical-operators)
