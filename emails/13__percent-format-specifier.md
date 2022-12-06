## Question

A student is working on a tip calculator program shown below:

```python
bill_amount = 34
tip_percentage = 0.2
total = bill_amount + (bill_amount * tip_percentage)

print(f"With a ${bill_amount} bill and a {tip_percentage * 100}% tip, your total is ${total}")
```

The output they want is:

```text
With a $34 bill and a 20% tip, your total is $40.80
```

The output they have now is:

```text
With a $34 bill and a 20.0% tip, your total is $40.8
```

In Python, there's a [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language) you can use to format data in `f-strings`. How could we use it here to get the desired output?

## Answer

```python
bill_amount = 34
tip_percentage = 0.2
total = bill_amount + (bill_amount * tip_percentage)

print(f"With a ${bill_amount} bill and a {tip_percentage:.0%} tip, your total is ${total:.2f}")
```

## Explanation

You add format specifiers using the `:` character. The `.` is used to determine the number of digits after the decimal point in a `float`. The `%` multiplies the variable by 100 and adds the `%` sign. The `f` is used to ensure the number is given fixed-point notation. 

## Resources

-   [The Python Docs - Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
