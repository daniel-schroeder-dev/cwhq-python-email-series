## Question

A programmer is working on an app that formats US phone numbers. There are four parts to a US phone number:

+32 - (217) - 990 - 1423

+32  => Country Code
217  => Area Code
990  => Telephone Prefix
1423 => Line Number

They want to create a function that will format any US phone number, and they want whoever uses the function to be able to pass in the numbers only (no + or ()). They also want to be able to format a number in three different forms:

990-1423             =>                            Telephone Prefix - Line Number
(217)-990-1423       =>                Area Code - Telephone Prefix - Line Number
+32-(217)-990-1423   => Country Code - Area Code - Telephone Prefix - Line Number

This is their first attempt at solving the problem using Python:

```python
def format_us_phone_number_1(telephone_prefix, line_number):
    phone_number = []
    phone_number.append(str(telephone_prefix))
    phone_number.append(str(line_number))

    return "-".join(phone_number)


def format_us_phone_number_2(telephone_prefix, line_number, area_code):
    phone_number = []

    if area_code:
        area_code = f"({area_code})"
        phone_number.append(area_code)

    phone_number.append(str(telephone_prefix))
    phone_number.append(str(line_number))

    return "-".join(phone_number)


def format_us_phone_number_3(telephone_prefix, line_number, area_code, country_code):
    phone_number = []

    if country_code:
        country_code = f"+{country_code}"
        phone_number.append(country_code)

    if area_code:
        area_code = f"({area_code})"
        phone_number.append(area_code)

    phone_number.append(str(telephone_prefix))
    phone_number.append(str(line_number))

    return "-".join(phone_number)


formatted_number = format_us_phone_number_1(990, 1423)
print(formatted_number)  # 990-1423

formatted_number = format_us_phone_number_2(990, 1423, 217)
print(formatted_number)  # (217)-990-1423
    
formatted_number = format_us_phone_number_3(990, 1423, 217, 32)
print(formatted_number)  # +32-(217)-990-1423
```

Research default parameters in Python to see if there's a way to write a single function to solve this problem!


## Answer

```python
def format_us_phone_number(telephone_prefix, line_number, area_code=None, country_code=None):
    phone_number = []

    if country_code:
        country_code = f"+{country_code}"
        phone_number.append(country_code)

    if area_code:
        area_code = f"({area_code})"
        phone_number.append(area_code)

    phone_number.append(str(telephone_prefix))
    phone_number.append(str(line_number))

    return "-".join(phone_number)


formatted_number = format_us_phone_number(990, 1423)
print(formatted_number)  # 990-1423

formatted_number = format_us_phone_number(990, 1423, 217)
print(formatted_number)  # (217)-990-1423
    
formatted_number = format_us_phone_number(990, 1423, 217, 32)
print(formatted_number)  # +32-(217)-990-1423
```

## Explanation

You can provide default values for certain parameters using the syntax `parameter=value`. This allows you to leave out those arguments when calling the function if you'd like to use the default value instead.

## Resources

-   [The Python Tutorial - Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)
