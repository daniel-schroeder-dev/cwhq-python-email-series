## Question

A young Python programmer is working on a program to help them with their geometry homework. They are testing their results against the [Desmos Online Calculator](https://www.desmos.com/scientific) and can't seem to calculate the area of a circle with the same precision or accuracy as that calculator. 

Here's their attempt at calculating the area of a circle:

```python
def calculate_circle_area(radius):
    pi = 3.14159
    return pi * radius ** 2


radius = 3
circle_area = calculate_circle_area(radius)

print(circle_area)  # 28.27431
```

Their result (28.27431) is slightly different than what they see online (28.27433388). They guess that they probably need more precision with their `pi` constant, but aren't sure how much. A more experienced Python programmer looks over their program and tells them to study Python's `math` module for a possible solution. Research the `math` module and see if you can find an easier way to calculate PI.

## Answer

```python
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2


radius = 3
circle_area = calculate_circle_area(radius)

print(circle_area)  # 28.274333882308138
```
## Explanation

Using the `math.pi` constant, you can get much more precise calculations. There are many other helpful functions and constants in the `math` module, so explore it any time you're working with math in Python!

## Resources

-   [The Python Docs - `math.pi`](https://docs.python.org/3/library/math.html#math.pi)
