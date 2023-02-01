## Question

A programmer is working on an app that validates email addresses and needs to pull the domain name (the part after the `@` symbol) from a list of email addresses.

Here's the way they are doing things currently:

```python
def get_domains(email_addresses):
    domains = []
    for email_address in email_addresses:
        at_symbol_index = email_address.index("@")
        domain = ""
        for index in range(at_symbol_index + 1, len(email_address)):
            domain += email_address[index]

        domains.append(domain)

    return domains


email_addresses = [
    "steve@aol.com",
    "jess@school.mit.edu",
    "django@python.net",
]

domains = get_domains(email_addresses)
print(domains) # ['aol.com', 'school.mit.edu', 'python.net']
```

Research slicing operations in Python and see if you can refactor the `get_domains()` function using slicing techniques.

## Answer

```python
def get_domains(email_addresses):
    domains = []
    for email_address in email_addresses:
        at_symbol_index = email_address.index("@")
        # Using slice operators saves us from looping again!
        domain = email_address[at_symbol_index + 1:]
        domains.append(domain)

    return domains


email_addresses = [
    "steve@aol.com",
    "jess@school.mit.edu",
    "django@python.net",
]

domains = get_domains(email_addresses)
print(domains) # ['aol.com', 'school.mit.edu', 'python.net']
```

## Explanation

You can use slicing to pull characters from a `str` without having to use a loop. The slicing syntax also works with `lists`!

## Resources

-   [Real Python - String Slicing](https://realpython.com/python-strings/#string-slicing)
