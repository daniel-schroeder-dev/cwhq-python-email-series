## Question

A young Python programmer is working on an app that will randomly shuffle the letters of a word and have the user guess the word. They're writing their own shuffling algorithm and have got a working version, which you can see below:

```python
from random import randint


def shuffle_letters(word):
    letters = list(word)
    shuffled_letters = []
    for _ in range(len(letters)):
        random_index = randint(0, len(letters) - 1)
        random_letter = letters.pop(random_index)
        shuffled_letters.append(random_letter)

    return "".join(shuffled_letters)


print(shuffle_letters("banana"))  # aabnan
print(shuffle_letters("pizza"))  # zapiz
```

Their program works, and they show it to a more experienced Python programmer. While impressed with their algorithm, the elder Python programmer suggests that there's an easier way to shuffle the letters in the word provided by the [random](https://docs.python.org/3/library/random.html) module. Investigate the functions provided by this module and see if you can help them refactor their program! 

## Answer

```python
from random import sample


def shuffle_letters(word):
    shuffled_letters = sample(word, k=len(word))
    return "".join(shuffled_letters)


print(shuffle_letters("banana"))  # aabnan
print(shuffle_letters("pizza"))  # zapiz
```

## Explanation

The `sample()` function from the `random` module allows you to shuffle the letters of a `str`. It might seem like the `shuffle()` function would be the appropriate function to shuffle a `str`, but since `str` are immutable (can't be changed) you have to use `sample()` and then convert the returned `list` to a `str` using the `str.join()` method.

## Resources

-   [The Python Docs - `sample()`](https://docs.python.org/3/library/random.html#random.sample)
