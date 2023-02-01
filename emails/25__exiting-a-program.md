## Question

A new Python programmer is working on an app and adds the following logic:

```python
admin_username = "admin"
admin_password = "$3cr3T"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username != admin_username or password != admin_password:
    print("Sorry, you can't use this app!")
else:
    print("OK, you can use this app!")
    # The rest of the program logic now lives in this `else` clause

```

Notice that if the user provides the correct login credentials, they can use the app, but all of the apps code will have to be included in the `else` clause of the conditional statement. 

Can you think of a better way to organize this program?

## Answer

```python
# The `exit` function from the `sys` module let's you quit a program.
from sys import exit

admin_username = "admin"
admin_password = "$3cr3T"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username != admin_username or password != admin_password:
    print("Sorry, you can't use this app!")
    # The program will end here.
    exit()


# We don't have to use an `else` clause now!
print("OK, you can use this app!")
```

## Explanation

The `exit()` function from the `sys` module allows you to exit a program.

## Resources

-   [The Python Docs - `sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit)
