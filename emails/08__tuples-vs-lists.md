## Question

Python's native `list` and `tuple` data structures are used to store multiple values. A `list` can be changed after creation, but a `tuple` cannot. Besides the fact that `lists` can be changed, they also normally represent a group of homogeneous (of the same kind) data. So, a `list` of usernames, or a `list` of items in a shopping cart makes sense. In contrast, `tuples` are normally used to represent a group of heterogeneous (diverse in kind) data, and can be thought of as a keyless `dict`. So, while a `list` contains many related things, a `tuple` contains many data points about a single thing. 

Given the information above, which data structure best-fits the following scenarios:
- All of the menu items in an online store
- The transaction amounts of a credit card on a banking website
- Information about a movie on a streaming website like Netflix
- All of the text messages between two users of a messaging app
- The contact details of a user on a messaging app


## Answer

Best-fit is a `list`:
- All of the menu items in an online store
- The transaction amounts of a credit card on a banking website
- All of the text messages between two users of a messaging app

Best-fit is a `tuple`:
- Information about a movie on a streaming website like Netflix
- The contact details of a user on a messaging app


## Explanation

The `list` items are all of the same type of thing (menu items, transaction amounts, text messages). Each slot in the `list` will be exactly the same type of data as the next, but the values themselves will be different. 

The `tuple` items are all data points of possibly different types representing information about a single thing (movie data or contact details). Each slot in the `tuple` has a unique meaning and isn't merely a different form of the values in other slots.

## Resources

-   [The Python Standard Library Documentation - Lists](https://docs.python.org/3/library/stdtypes.html#lists)
-   [The Python Standard Library Documentation - Tuples](https://docs.python.org/3/library/stdtypes.html#tuples)
