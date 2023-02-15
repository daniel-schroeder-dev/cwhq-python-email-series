## Question

A young Pythonista has written a bookmark manager program that allows them to quickly browse bookmarks and get the relevant URL to the webpage. They've created a function that allows a user to search for a bookmark by the `site_name` and then it displays the relevant `url` which they can then copy/paste into a web browser. Here are the basics of how the `bookmarks` look and how the `get_bookmark()` function works:

```python
def get_bookmark(site_name):
    for bookmark in bookmarks:
        if site_name in bookmark.values():
            print(f"{site_name}'s URL is: {bookmark['url']}")
            break
    else:
        print(f"Bookmark not found for {site_name}!")


bookmarks = [
    {
        "site_name": "Python Homepage",
        "url": "https://www.python.org",
    },
    {
        "site_name": "Real Python",
        "url": "https://realpython.com",
    },
    {
        "site_name": "The Hitchhiker's Guide to Python",
        "url": "https://docs.python-guide.org",
    },
]

get_bookmark("Real Python")  # Real Python's URL is: https://realpython.com
get_bookmark("Fake Python")  # Bookmark not found for Fake Python!
```

This program works as expected, but an experienced Pythonista sees their work and suggests a cleaner implementation using the [webbrowser](https://docs.python.org/3/library/webbrowser.html) module. Research this module and see if you can find a way to use it to make this program work better!

## Answer

```python
from webbrowser import open_new

def get_bookmark(site_name):
    for bookmark in bookmarks:
        if site_name in bookmark.values():
            open_new(bookmark["url"])
            break
    else:
        print(f"Bookmark not found for {site_name}!")


bookmarks = [
    {
        "site_name": "Python Homepage",
        "url": "https://www.python.org",
    },
    {
        "site_name": "Real Python",
        "url": "https://realpython.com",
    },
    {
        "site_name": "The Hitchhiker's Guide to Python",
        "url": "https://docs.python-guide.org",
    },
]

get_bookmark("Real Python")  # Open's the website in the user's default browser
get_bookmark("Fake Python")  # Bookmark not found for Fake Python!
```

## Explanation

The `open_new()` function in the `webbrowser` module allows you to open a URL in the user's default browser.

## Resources

-   [The Python Docs - `webbrowser.open_new()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.open_new)
