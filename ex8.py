# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]


def sum_total_price(products):
    return sum(product["price"] for product in products)

# Example usage
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]

total_price = sum_total_price(products)
print("Total price:", total_price)

