## Question

A young Pythonista is working on a program to help them with their statistics homework. They've created two helper-functions to calculate the `mean()` and `median()` like so:

```python
def mean(nums):
    return sum(nums) / len(nums)


def median(nums):
    middle_index = (len(nums) - 1) // 2
    if len(nums) % 2 != 0:
        return nums[middle_index]

    return mean(nums[middle_index:middle_index + 2])


print(mean([1, 2, 3, 4, 4]))  # 2.8


median_value =  median([1, 3, 5])
print(median_value)  # 3

median_value =  median([1, 3, 5, 7])
print(median_value)  # 4.0
```

They are happy with their implementation, but a more experienced Pythonista tells them that these functions already exist in the [Python standard library](https://docs.python.org/3/library/index.html). Search through this library (CTRL+F makes this easier) to see if you can find the correct module where these functions may live. If you find the module, import the correct functions and refactor the program above to use them.

## Answer

```python
from statistics import mean, median


print(mean([1, 2, 3, 4, 4]))  # 2.8

median_value =  median([1, 3, 5])
print(median_value)  # 3

median_value =  median([1, 3, 5, 7])
print(median_value)  # 4.0
```

## Explanation

The `statistics` module has useful helper-functions for common statistics tasks. Use it the next time you need help with your statistics homework!

## Resources

-   [The Python Docs - `statistics`](https://docs.python.org/3/library/statistics.html#module-statistics)
