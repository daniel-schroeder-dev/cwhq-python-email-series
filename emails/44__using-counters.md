## Question

A young Python programmer is working on a program that counts the number of occurrences of every letter in the alphabet in a given sentence. This is their implementation so far:

```python
from string import ascii_lowercase

def count_num_letters(sentence):
    count_letters = dict.fromkeys(ascii_lowercase, 0)
    for letter in sentence.lower():
        if letter.isalpha():
            count_letters[letter] += 1

    print(f"Count of different letters in '{sentence}':")
    for letter, count in count_letters.items():
        if count > 0:
            print(letter, count)



count_num_letters("Hey, what's up?")
```

*output*
```text
Count of different letters in 'Hey, what's up?':
a 1
e 1
h 2
p 1
s 1
t 1
u 1
w 1
y 1
```

They are pleased that their algorithm works correctly! A more experienced Python programmer sees their work and praises the implementation, but points out that there's an easier way to solve this problem in Python. Investigate the [collections](https://docs.python.org/3/library/collections.html) module and see if you can find a way to refactor the `count_num_letters()` function to use built-in Python functions/classes to perform this task. 

## Answer

```python
from collections import Counter


def count_num_letters(sentence):
    count_letters = Counter(sentence.lower())

    print(f"Count of different letters in '{sentence}':")
    for letter, count in count_letters.items():
        if count > 0 and letter.isalnum():
            print(letter, count)


count_num_letters("Hey, what's up?")
```

*output*
```text
Count of different letters in 'Hey, what's up?':
h 2
e 1
y 1
w 1
a 1
t 1
s 1
u 1
p 1
```

## Explanation

The `Counter` class of the `collections` module is an easy way to count the number of occurrences of letters in a `str`.

## Resources

-   [The Python Docs - Counter objects](https://docs.python.org/3/library/collections.html#counter-objects)
