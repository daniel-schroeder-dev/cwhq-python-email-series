## Question

A young Pythonista is working on a program that works with social security numbers for a government website. Their job is to take numbers in this form xxx-xx-xxxx and change them to this form xxx xx xxx. So, they need to replace the "-" characters with an empty space. Here's their first attempt:

```python
def sanitize_ssn_number(ssn_number):
    sanitized_ssn_number = ""

    for token in ssn_number:
        if token == "-":
            token = " "
        sanitized_ssn_number += token

    return sanitized_ssn_number


ssn_numbers = [
    "232-33-8344",
    "834-24-8211",
    "882-35-8174",
]

sanitized_ssn_numbers = []
for ssn_number in ssn_numbers:
    sanitized_ssn_number = sanitize_ssn_number(ssn_number)
    sanitized_ssn_numbers.append(sanitized_ssn_number)


print(sanitized_ssn_numbers)  # ['232 33 8344', '834 24 8211', '882 35 8174']
```

An experienced Pythonista sees their code and notices they could completely remove the `sanitize_ssn_number()` function if they used a built-in string method to replace the "-" character with a " ". Research the different [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods) and see if you can refactor their program to use the correct one.

## Answer

```python
ssn_numbers = [
    "232-33-8344",
    "834-24-8211",
    "882-35-8174",
]

sanitized_ssn_numbers = []
for ssn_number in ssn_numbers:
    sanitized_ssn_number = ssn_number.replace("-", " ")
    sanitized_ssn_numbers.append(sanitized_ssn_number)


print(sanitized_ssn_numbers)  # ['232 33 8344', '834 24 8211', '882 35 8174']
```

## Explanation

The `str.replace()` method makes it trivial to replace all occurrences of a character in a `str`. 

## Resources

-   [The Python Docs - `str.replace()`](https://docs.python.org/3/library/stdtypes.html#str.replace)
