## Question

To read or write files in Python, you use the `open()` function from the Python standard library. Imagine we have this file containing usernames:

*users.txt*

```text
djs
sahibk
inder
margaret
```

To open that file and read the data from Python, we could use this pattern:

```python
file_handle = open("users.txt", mode="rt")  # Opens `users.txt` in read text (rt) mode.
file_text = file_handle.read()

print(file_text)

file_handle.close()
```

However, there's a problem with the approach used above. We have to remember to manually close the `file_handle`. If we forget, and we have other code running that interacts with the filesystem, we could run into issues because there are a limited number of file handles that our given out to running programs.

Research how using a context manager could automatically deal with closing a file handle and refactor the above example to use this pattern.

## Answer

```python
with open("users.txt", mode="rt") as file_handle:
    file_text = file_handle.read()
    print(file_text)

# No need to call `file_handle.close()`!
```

## Explanation

Using Python's `with` statement (which activates a Context Manager), we can safely read and write files. The `with` statement guarantees that no matter what happens, the `file_handle` returned from `open()` will be released back to the operating system.

## Resources

-   [The Python Tutorial - Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
