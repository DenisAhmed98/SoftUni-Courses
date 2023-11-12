products_dictionary = {}
while True:
    current_product = input().split(" ")
    product = current_product[0]

    if product == "buy":
        break

    price = current_product[1]
    quantity = current_product[2]
    price = float(price)
    quantity = int(quantity)

    if product not in products_dictionary.keys():
        products_dictionary[product] = []
        products_dictionary[product].extend([0, 0])
    products_dictionary[product][0] = price
    products_dictionary[product][1] += quantity

for key, value in products_dictionary.items():
    print(f"{key} -> {value[0]*value[1]:.2f}")