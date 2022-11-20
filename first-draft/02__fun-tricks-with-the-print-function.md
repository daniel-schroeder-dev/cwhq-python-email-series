# Fun Tricks With Python's `print()` Function

To display text on the screen in a Python program, you use the `print()` function.

Most programs are fine simply adding whatever items you want to print inside the `print()` function as a single argument, as in the example below:

```python
favorite_foods = ["tacos", "burritos", "nachos"]
numbers = "123456789"
phrase = "You're not gonna need it"

print(favorite_foods)
print(numbers)
print(phrase)
```

*Output*

```text
['tacos', 'burritos', 'nachos']
123456789
You're not gonna need it
```

## Using The Splat Operator

The first trick you can use with `print()` is one that isn't unique to this function, but instead takes advantage of the fact that the `print()` function happens to accept a variable number of arguments to display on the page.

For example, we could display the items in our `favorite_foods` `list` next to each other like this:

```python
favorite_foods = ["tacos", "burritos", "nachos"]

print(favorite_foods[0], favorite_foods[1], favorite_foods[2])
```

*Output*

```text
tacos burritos nachos
```

Since we can pass *any* number of arguments to `print()`, we can use the `*` operator (often referred to as the *splat* operator) to unpack the items in a `list` instead of accessing them individually by index number.

Using the splat operator, our previous example could be shortened to:


```python
favorite_foods = ["tacos", "burritos", "nachos"]

print(*favorite_foods)
```

*Output*

```text
tacos burritos nachos
```

The splat operator works with `str` data as well. Instead of displaying the whole `str` at once, each character of the `str` will be displayed separated by a space:


```python
numbers = "123456789"
phrase = "You're not gonna need it"

print(numbers)
print(phrase)
```

*Output*

```text
1 2 3 4 5 6 7 8 9
Y o u ' r e   n o t   g o n n a   n e e d   i t
```

## Adding Custom Separators With The `sep` Parameter

The splat operator lets you add a space between items in a `list` or letters in a `str`, but what if you wanted to add a different separator between items?

For example, to put dashes between the items in our `favorite_foods` `list`, we could do this:


```python
favorite_foods = ["tacos", "burritos", "nachos"]

print(favorite_foods[0], "-", favorite_foods[1], "-", favorite_foods[2])
```

*Output*

```text
tacos - burritos - nachos
```

Using the `sep` parameter, which is a keyword argument to `print()`, and the splat operator, we can accomplish the same thing with much less hassle:


```python
favorite_foods = ["tacos", "burritos", "nachos"]

print(*favorite_foods, sep=" - ")
```

*Output*

```text
tacos - burritos - nachos
```

Of course, the same technique works for `str` data as well:


```python
numbers = "123456789"
phrase = "You're not gonna need it"

print(*numbers, sep=" + ")
print(*phrase, sep="_")
```

*Output*

```text
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
Y_o_u_'_r_e_ _n_o_t_ _g_o_n_n_a_ _n_e_e_d_ _i_t
```

The examples above also show that you can use any combinations of characters you want in the `sep` parameter.

## Using The `end` Parameter 

Usually, data that you `print()` is separated from the next `print()` call by a newline.

For example:

```python
print("Hello")
print("World")
```

*Output*

```text
Hello
World
```

The `end` parameter of the `print()` function can be used to change the character that occurs *between* consecutive calls the to the `print()` function.

For example:

```python
print("Hello", end="")
print("World")
```

*Output*

```text
HelloWorld
```

This may not seem useful at first, but consider this example, where the `build_pyramid()` function utilizes the `end` parameter to ensure that no newlines are added while adding the bricks (represented by the "^" character) in each row of the pyramid:

```python
def build_pyramid(height):
    num_bricks = height * 2

    for row in range(1, num_bricks, 2):
        spaces = " " * (num_bricks - row + 1)
        print(spaces, end="")
        for _ in range(row):
            print('^ ', end="")
        print()

    print()


build_pyramid(3)
build_pyramid(6)
build_pyramid(12)
```

*Output*

```text
      ^
    ^ ^ ^
  ^ ^ ^ ^ ^

            ^
          ^ ^ ^
        ^ ^ ^ ^ ^
      ^ ^ ^ ^ ^ ^ ^
    ^ ^ ^ ^ ^ ^ ^ ^ ^
  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

                        ^
                      ^ ^ ^
                    ^ ^ ^ ^ ^
                  ^ ^ ^ ^ ^ ^ ^
                ^ ^ ^ ^ ^ ^ ^ ^ ^
              ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
            ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
          ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
        ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
      ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
    ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
```

## Summary

As you can see, there's more to `print()` than simply displaying text to the screen! By utilizing the splat operator and the `sep` and `end` parameters of the `print()` function, you can create a wide variety of interesting outputs in your programs!
