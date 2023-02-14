def sort_by_price(item):
    return item["price"]


shopping_cart = [
    {
        "item_name": "XBox 720",
        "price": 799.99,
    },
    {
        "item_name": "Logitech Wireless Mouse",
        "price": 45.75,
    },
    {
        "item_name": "Mechanical Keyboard",
        "price": 245.50,
    },
]


sorted_shopping_cart = sorted(shopping_cart, key=sort_by_price)  

print(sorted_shopping_cart)
