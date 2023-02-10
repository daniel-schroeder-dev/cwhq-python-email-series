
def get_unique_customers(customers):
    unique_customers = []
    for customer in customers:
        if customer not in unique_customers:
            unique_customers.append(customer)

    return unique_customers


customers = ["Bob Smith", "Janice Carencrow", "Jasper Rothchild", "Bob Smith"]
unique_customers = get_unique_customers(customers)

print(unique_customers)


customers = ["Bob Smith", "Janice Carencrow", "Jasper Rothchild", "Bob Smith"]
unique_customers = set(customers)

print(unique_customers)  # ['Bob Smith', 'Janice Carencrow', 'Jasper Rothchild']
