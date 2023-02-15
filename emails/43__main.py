def bankers_round(number):
    rounded_number = None
    # Gives a rounded down integer of the number
    rounded_down_number = int(number)
    fractional_part = number - rounded_down_number

    if fractional_part > 0.5:
        rounded_number = rounded_down_number + 1
    elif fractional_part < 0.5:
        rounded_number = rounded_down_number
    # Banker's round takes effect
    elif fractional_part == 0.5:
        # If the rounded down number is even
        if rounded_down_number % 2 == 0:
            rounded_number = rounded_down_number
        else:
            rounded_number = rounded_down_number + 1

    return rounded_number



print(bankers_round(1.1))  # 1
print(bankers_round(1.5))  # 2
print(bankers_round(1.6))  # 2

print(bankers_round(2.1))  # 2
print(bankers_round(2.5))  # 2
print(bankers_round(2.6))  # 3


print(round(1.1))  # 1
print(round(1.5))  # 2
print(round(1.6))  # 2

print(round(2.1))  # 2
print(round(2.5))  # 2
print(round(2.6))  # 3
