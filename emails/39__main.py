def get_absolute_value(number):
    if number < 0:
        number *= -1

    return number

number = -3
absolute_value = get_absolute_value(number)

print(f"The absolute value of {number} is {absolute_value}.")

number = 3
absolute_value = get_absolute_value(number)

print(f"the absolute value of {number} is {absolute_value}.")


number = -3
absolute_value = abs(number)

print(f"The absolute value of {number} is {absolute_value}.")  # The absolute value of -3 is 3.

number = 3
absolute_value = abs(number)

print(f"The absolute value of {number} is {absolute_value}.")  # The absolute value of 3 is 3.
