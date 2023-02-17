## Question


A young Pythonista is making a program where a user has to form words using unique letters of the alphabet for each word (all lowercase letters). They get a point for each letter they use, and they can't use the same letter twice in one word or between words. To make sure the user is only pulling from the list of available words, the programmer has created a list of all the letters in the alphabet using this function: 


```python
def create_lowercase_letters():
    lowercase_letters = []

    # The Unicode code point of "a" is 97
    # The Unicode code point of "z" is 122
    # This loop will give us the character codes from a-z or 97-122
    for character_code in range(97, 123):
        # The chr() function turns a character code into a letter
        # So, chr(97) would be the letter "a"
        lowercase_letters.append(chr(character_code))

    return lowercase_letters


lowercase_letters = create_lowercase_letters()
```

The young programmer is pleased with their algorithm, but a more experienced Pythonista comes along and gives them some advice. They suggest looking into the `string` module to see if there's a way to get all of the lowercase letters without having to build a function to do so. They also tell the young programmer that the `list()` built-in function will come in handy. Investigate the [string](https://docs.python.org/3/library/string.html) module and see if you can find a way to replace the `create_lowercase_letters()` function.

## Answer

```python
from string import ascii_lowercase


lowercase_letters = list(ascii_lowercase)
```

## Explanation

You can get a string of all the lowercase letters of the alphabet from the `string` module's `ascii_lowercase` constant. When you pass a `str` to the `list()` function, each letter of the `str` will be a slot in the list.

## Resources

-   [The Python Docs - `string.ascii_lowercase`](https://docs.python.org/3/library/string.html#string.ascii_lowercase)
