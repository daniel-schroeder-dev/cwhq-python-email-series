# Using Trailing Commas to Prevent Common Errors

Python's `list` data structure is a handy way to store multiple items in a single container. 

For example, if you wanted to keep track of a `list` of your hobbies, you could write the following code:

```python
hobbies = [
    "Coding",
    "Reading",
    "Running",
    "Traveling",
]
```
 
You don't have to write a `list` on multiple lines (as in the example above), but it helps readability for long lists to keep each item on its own line. Python doesn't care how you write it, and when you display a `list` using the `print()` function, all items are on the same line (the double-quotes also become single-quotes, but that's for another discussion):

```python
hobbies = [
    "Coding",
    "Reading",
    "Running",
    "Traveling",
]

print(hobbies)
```

*Output*

```text
['Coding', 'Reading', 'Running', 'Traveling']
```

## Trailing Commas

The final comma (known as a _trailing comma_) is optional, but it helps prevent a tricky error when your `list` contains `str` data. 

To see an example of what can happen when you leave off the final comma, consider the same `list` of `hobbies` from above but without the trailing comma:

```python
hobbies = [
    "Coding",
    "Reading",
    "Running",
    "Traveling"  # No trailing comma
]

print(hobbies)
```

*Output*

```text
['Coding', 'Reading', 'Running', 'Traveling']
```

The `list` is displayed the same way. What would happen if, later on, we want to add a new hobby to our `hobbies` `list`, such as "Swimming"? 

We may accidentally forget to add the comma after "Traveling", like this:

```python
hobbies = [
    "Coding",
    "Reading",
    "Running",
    "Traveling"  # Uh oh, we forgot the comma!
    "Swimming"
]

print(hobbies)
```

*Output*

```text
['Coding', 'Reading', 'Running', 'TravelingSwimming']
```

Did you notice that the final item in our `list` is "TravelingSwimming" instead of "Swimming"? Our `list` of `hobbies` does not contain what we expect, but Python doesn't throw an error to tell us! 

## String Concatenation in Python

This odd behavior occurs because, in Python, you can concatenate (glue together) two strings by placing them next to each other, like this:

```python
name = "John" "Doe"

print(name)
```

*Output*

```text
JohnDoe
```

Since we didn't put a comma between the items in our `hobbies` `list`, and Python doesn't care about each item being on its own line, we've effectively done this:

```python
                                         # These are concatenated!
hobbies = ["Coding", "Reading", "Running", "Traveling" "Swimming"]
```

## Trailing Commas Prevent Silly Errors

All this pain could've been avoided if we'd always used a trailing comma! 

Remember, this was our original `hobbies` `list`:

```python
hobbies = [
    "Coding",
    "Reading",
    "Running",
    "Traveling",
]
```

Adding "Swimming" to the above `list` is no problem when there's a trailing comma:


```python
hobbies = [
    "Coding",
    "Reading",
    "Running",
    "Traveling",  # This is already here, so no issue!
    "Swimming",   # Keep the good habits going by adding a trailing comma.
]

print(hobbies)
```

*Output*

```text
['Coding', 'Reading', 'Running', 'Traveling', 'Swimming']
```

## What Happens When a `list` Contains Other Data Types?

If your `list` contains items other than `str` data, then Python will throw an error if you forget to add a comma between items. The error can be a bit confusing if you use an older version of Python, though!

Consider this `list` representing the ages of a group of students and not containing a trailing comma:

```python
student_ages = [
    13,
    14,
    11,
    16  # No trailing comma!
]

print(student_ages)
```

*Output*

```text
[13, 14, 11, 16]
```

If we add another age later on and forget to add the comma after `16`, then an error will occur:


```python
student_ages = [
    13,
    14,
    11,
    16  # No trailing comma!
    17  # Uh oh...
]

print(student_ages)
```

*Output*

```text
  File "list-basics.py", line 5
    16  # No trailing comma!
    ^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

Depending on your version of Python (the above was run with Python 3.11) the error message may be less helpful. For example, in Python 3.7, this is the error message:

```text
  File "list-basics.py", line 6
    17  # Uh oh...
     ^
SyntaxError: invalid syntax
```

Notice there's no hint, such as "Perhaps you forgot a comma?" when using this older Python version. 

## Summary

Hopefully, these examples have convinced you of the need for using a trailing comma in your `lists`! There are no downsides to using them (other than typing an extra character), and they can help prevent errors when adding new items to a `list` as you're working on a program. There are so many errors that can crop up when you're writing a program; prevent as many as you can through good habits and your programming life will be easier! 

