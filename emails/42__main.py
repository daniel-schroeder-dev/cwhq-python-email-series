ssn_numbers = [
    "232-33-8344",
    "834-24-8211",
    "882-35-8174",
]

sanitized_ssn_numbers = []
for ssn_number in ssn_numbers:
    sanitized_ssn_number = ssn_number.replace("-", " ")
    sanitized_ssn_numbers.append(sanitized_ssn_number)


print(sanitized_ssn_numbers)  # ['232 33 8344', '834 24 8211', '882 35 8174']
