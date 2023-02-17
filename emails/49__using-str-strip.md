## Question

A young Pythonista is working on a program where user's can register with a username and password. To make sure the username/password don't have spaces at the beginning or end, they've written this `remove_spaces()` function:

```python
def remove_spaces(word):
    first_letter_found = False
    word_without_spaces = ""

    for position, letter in enumerate(word):
        if first_letter_found and letter.isspace() and word[position:].isspace():
            break

        if not letter.isspace():
            first_letter_found = True

        if first_letter_found:
            word_without_spaces += letter

    return word_without_spaces


username = "  steve9000   "
username = remove_spaces(username)

print(username)  # steve9000
print(len(username))  # 9
```

They test the function and it seems to work fine. A more experienced Pythonista sees their implementation and praises their algorithm and skills, but points out that they could remove this function entirely by using one of the [built-in `str` methods](https://docs.python.org/3/library/stdtypes.html#string-methods). Investigate the built-in `str` methods and see if you can find a way to replace the `remove_spaces()` function. 

## Answer

```python
username = "  steve9000   "
username = username.strip()

print(username)  # steve9000
print(len(username))  # 9
```

## Explanation

The `str.strip()` method is a handy way to remove any characters from both sides of a `str`. If you don't pass an argument in the parentheses, it removes spaces.

## Resources

-   [The Python Docs - `str.strip()`](https://docs.python.org/3/library/stdtypes.html#str.strip)
