## Question

A young Python programmer is working on a program that allows users to store contact information for their friends and family. They are using a dictionary to store the contact information for each user, and each user has a few common keys, such as:

- `full_name`
- `phone_number`

Some users have additional details such as:

- `email_address`
- `home_address`

In the program, the programmer wants to display contact details like this:

```text
******** PRIMARY CONTACT DETAILS ************

Name: John Smith
Phone Number: 323-8832

*********************************************

******* SECONDARY CONTACT DETAILS ***********

Email Address: jdawg@aol.com
Home Address: None

*********************************************
```

Note that if a particular key doesn't have a value, they want to show "None" (such as the `home_address` field above).

Here's what they've got so far:


```python
def display_contact_details(contact_information):
    full_name = contact_information["full_name"]
    phone_number = contact_information["phone_number"]
    email_address = None
    home_address = None

    if "email_address" in contact_information:
        email_address = contact_information["email_address"]

    if "home_address" in contact_information:
        home_address = contact_information["home_address"]

    contact_details = f"""
        ******** PRIMARY CONTACT DETAILS ************

        Name: {full_name}
        Phone Number: {phone_number}

        *********************************************

        ******* SECONDARY CONTACT DETAILS ***********

        Email Address: {email_address}
        Home Address: {home_address}

        *********************************************
    """
    print(contact_details)



contacts = [
        {
            "full_name": "John Smith",
            "phone_number": "323-8832",
            "email_address": "jdawg@aol.com",
        },
        {
            "full_name": "Jane Doe",
            "phone_number": "341-9231",
            "email_address": "jane@hotmail.com",
            "home_address": "142 Emoji Lane",
        },
]


for contact in contacts:
    display_contact_details(contact)

```

This works as expected, but an older Python programmer happens to see their work and takes issue with this section:

```python
def display_contact_details(contact_information):

    email_address = None
    home_address = None

    if "email_address" in contact_information:
        email_address = contact_information["email_address"]

    if "home_address" in contact_information:
        home_address = contact_information["home_address"]

```

The older Python programmer points out that there's no need for the conditional statements if you use the correct dictionary method to set the `email_address` and `home_address` variables. Investigate Python's [dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) data structure and see if you can refactor the `display_contact_details()` function to use a dictionary method to assign the `email_address` and `home_address` values.


## Answer

```python
def display_contact_details(contact_information):
    full_name = contact_information["full_name"]
    phone_number = contact_information["phone_number"]

    email_address = contact_information.get("email_address")
    home_address = contact_information.get("home_address")

    contact_details = f"""
        ******** PRIMARY CONTACT DETAILS ************

        Name: {full_name}
        Phone Number: {phone_number}

        *********************************************

        ******* SECONDARY CONTACT DETAILS ***********

        Email Address: {email_address}
        Home Address: {home_address}

        *********************************************
    """
    print(contact_details)



contacts = [
        {
            "full_name": "John Smith",
            "phone_number": "323-8832",
            "email_address": "jdawg@aol.com",
        },
        {
            "full_name": "Jane Doe",
            "phone_number": "341-9231",
            "email_address": "jane@hotmail.com",
            "home_address": "142 Emoji Lane",
        },
]


for contact in contacts:
    display_contact_details(contact)

```

## Explanation

Using `dict.get(key)` allows you to pull the value from the `dict` or `None` if there's no `key` in the `dict` by that name. This saves you from having to write code to check if a key is `in` a `dict` and then use conditional logic to pull the key from the `dict` if it is. 

## Resources

-   [The Python Docs - `dict.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get)
