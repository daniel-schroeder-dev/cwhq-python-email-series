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

