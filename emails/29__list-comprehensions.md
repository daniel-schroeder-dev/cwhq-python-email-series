## Question

Mapping and filtering are two common operations programmers need to perform on lists. Mapping is taking a list and changing the items in that list into a new form, and then putting these in a new list, as in the example below:

```python
nums = [2, 4, 6]
nums_squared = []

for num in nums:
    nums_squared.append(num ** 2)


print(nums_squared)  # [4, 16, 36]
```

When you run a filter, you build a new list with items from the original list removed, as in the example below that filters out even numbers:

```python
nums = [3, 4, 5, 6]
odd_nums = []

for num in nums:
    if num % 2 == 1:
        odd_nums.append(num)


print(odd_nums)  # [3, 5]
```

The above approaches work fine, but using list comprehensions, creating the mapped/filtered list could happen in a single line. Research how list comprehensions work and see if you can rewrite the above examples to create the `nums_squared` and `odd_nums` lists in a single line each.

## Answer

*map*
```python
nums = [2, 4, 6]

nums_squared = [num ** 2 for num in nums]
    
print(nums_squared)  # [4, 16, 36]
```

*filter*
```python
nums = [3, 4, 5, 6]

odd_nums = [num for num in nums if num % 2 == 1]

print(odd_nums)  # [3, 5]
```

## Explanation

List comprehensions can make map/filter operations much more compact. Once you get the hang of the syntax, you'll see that this form is often easier to read and less error-prone than the long-form versions.

## Resources

-   [Real Python - When to Use a List Comprehension in Python](https://realpython.com/list-comprehension-python/)
