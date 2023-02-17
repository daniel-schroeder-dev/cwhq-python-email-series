## Question

A young Pythonista is working on a program to count the number of vowels in a sentence. They are using a dictionary to count the number of occurrences of each vowel, and they need the dictionary to start with mappings from each vowel to the number 0 like this:

```python
vowel_counter = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}
```

While their implementation of `vowel_counter` is fine, a more experienced Pythonista sees their work and tells them there's an easier way to accomplish this using one of the built-in [dictionary methods](https://docs.python.org/3/library/stdtypes.html#dict). The fact that `list()` will turn a `str` into a `list` will also come in handy for a cleaner implementation. Research the built-in dictionary methods and see if you can refactor this program to create the `vowel_counter` in a single line. 

## Answer

```python
vowel_counter = dict.fromkeys(list("aeiou"), 0)
```


## Explanation

The `dict.fromkeys()` method let's you build a `dict` from a `list` of keys and then give each of those keys a default value (0 in our case).

## Resources

-   [The Python Docs - `dict.fromkeys()`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys)
