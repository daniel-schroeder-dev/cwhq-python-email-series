## Question

A young Python programmer is writing a program to help them track their best and worst times for running a mile (in minutes). To accomplish this task, they've created functions to find the best and worst running times from a list of running times:

```python
def find_best_running_time(running_times):
    # Start with a really high number, this would be over an hour.
    best_running_time = 100
    for running_time in running_times:
        if running_time < best_running_time:
            best_running_time = running_time

    return best_running_time


def find_worst_running_time(running_times):
    # Start with an impossibly low number.
    worst_running_time = 0
    for running_time in running_times:
        if running_time > worst_running_time:
            worst_running_time = running_time

    return worst_running_time


running_times = [10.1, 9.5, 11.2, 8.5, 10.5]

best_running_time = find_best_running_time(running_times)
worst_running_time = find_worst_running_time(running_times)

print(f"My best running time is {best_running_time} minutes.")  # My best running time is 8.5 minutes.
print(f"My worst running time is {worst_running_time} minutes.")  # My worst running time is 11.2 minutes.
```

An experienced Python programmer sees their work and comments: "You could accomplish both tasks with two built-in functions!". Research Python's built-in functions and see if you can find the two that could replace the `find_best_running_time()` and `find_worst_running_time` functions.


## Answer

```python
running_times = [10.1, 9.5, 11.2, 8.5, 10.5]

best_running_time = min(running_times)
worst_running_time = max(running_times)

print(f"My best running time is {best_running_time} minutes.")  # My best running time is 8.5 minutes.
print(f"My worst running time is {worst_running_time} minutes.")  # My worst running time is 11.2 minutes.
```

## Explanation

The `min()` and `max()` functions are handy Python built-in functions when you need to get the largest/smallest items from a list.

## Resources

-   [The Python Docs - `min()`](https://docs.python.org/3/library/functions.html#min)
-   [The Python Docs - `max()`](https://docs.python.org/3/library/functions.html#max)
