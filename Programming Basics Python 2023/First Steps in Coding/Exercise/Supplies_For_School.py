pack_of_pens = 5.80
pack_of_markers = 7.20
chemicals_per_liter = 1.20

num_of_pens = int(input())
num_of_markers = int(input())
liters_of_chemicals = int(input())
discount = int(input()) / 100

total_price = num_of_pens*pack_of_pens + num_of_markers*pack_of_markers + liters_of_chemicals*chemicals_per_liter
discount_price = total_price*discount
price_with_discount = total_price-discount_price

print(price_with_discount)