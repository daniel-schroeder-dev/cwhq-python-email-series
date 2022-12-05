## Question

When working with `tuples` that store information about a single entity, you may want to pull the individual values into variables to make them easier to work with. 

Consider this `user_data` `tuple` that holds username, password, age, and role data about a single user. If we wanted to work with these values in variables, we could write several lines of code like this: 

```python
user_data = "djs", "myp@$$w3rd", 36, "admin"

username = user_data[0]
password = user_data[1]
age = user_data[2]
role = user_data[3]
```

This is such a common task that Python provides a shorthand. Research multiple assignment in Python and see if you can find out how to pull all of the values from the above `user_data` `tuple` into variables in a single line.

## Answer

```python
user_data = "djs", "myp@$$w3rd", 36, "admin"

username, password, age, role = user_data
```

## Explanation

In Python, you can unpack all of the values from a `tuple` in a single line by separating each variable name with a comma and then writing the assignment expression. Note that this also works with `lists`, but `tuples` generally hold the kind of data (heterogeneous) that makes sense to unpack into variables.  

## Resources

-   [Real Python - Tuple Assignment, Packing, and Unpacking](https://realpython.com/lessons/tuple-assignment-packing-unpacking/)
