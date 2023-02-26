## Question

A young Python programmer is working on a password manager program for different websites they visit. They want to be able to display a password for a given website or put the message "Website not found for [site_name]" on the page if there's no entry for a given website. 

Here's what they have so far:

```python
def get_password(site_name):
    found_password = False

    for site_data in password_manager:
        if site_name in site_data.values():
            found_password = True
            print(f"The password for {site_name} is: {site_data['password']}")
            break

    if not found_password:
        print(f"No password found for {site_name}!")


password_manager = [
    {
        "site_name": "AOL Email",
        "password": "cds_in_the_mail",
    },
    {
        "site_name": "Instakilo",
        "password": "s0c!i@lm3d1@",
    },
    {
        "site_name": "CodeWizardsHQ",
        "password": "!lIk3<odin",
    },
]


get_password("CodeWizardsHQ")  # The password for CodeWizardsHQ is: !lIk3<odin
get_password("Gmail")  # No password found for Gmail!
```

Their program works as expected, but an experienced Python programmer tells them there may be a better way to deal with the `found_password` logic. Investigate [this section](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) of the Python Tutorial and see if there's a way to dispense with the `found_password` boolean flag altogether in this program!

## Answer

```python
def get_password(site_name):
    for site_data in password_manager:
        if site_name in site_data.values():
            print(f"The password for {site_name} is: {site_data['password']}")
            break
    else:
        print(f"No password found for {site_name}!")


password_manager = [
    {
        "site_name": "AOL Email",
        "password": "cds_in_the_mail",
    },
    {
        "site_name": "Instakilo",
        "password": "s0c!i@lm3d1@",
    },
    {
        "site_name": "CodeWizardsHQ",
        "password": "!lIk3<odin",
    },
]


get_password("CodeWizardsHQ")  # The password for CodeWizardsHQ is: !lIk3<odin
get_password("Gmail")  # No password found for Gmail!
```

## Explanation

When using a `for` loop in Python, you can attach an `else` clause that will only run if the loop finishes without encountering a `break` statement. This feature is a bit controversial, but it is a part of the language so you should be aware it exists!

## Resources

-   [The Python Tutorial - `break` and `continue` Statements, and `else` Clauses on Loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
