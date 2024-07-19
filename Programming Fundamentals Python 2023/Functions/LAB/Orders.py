product = input()
quantity = int(input())

def calculate_order(product,quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1.00
    elif product == "snacks":
        price = 2.0

    return quantity*price

order = calculate_order(product,quantity)

print(f"{order:.2f}")
