first_names = ["Daniel", "Jess", "Bob"]
last_names = ["Smith", "Fury", "Worth"]

full_names = []
for index, first_name in enumerate(first_names):
    last_name = last_names[index]
    full_names.append((first_name, last_name))
    

print(full_names) # [('Daniel', 'Smith'), ('Jess', 'Fury'), ('Bob', 'Worth')]


full_names = []
for first_name, last_name in zip(first_names, last_names):
    full_names.append((first_name, last_name))
    

print(full_names) # [('Daniel', 'Smith'), ('Jess', 'Fury'), ('Bob', 'Worth')]
