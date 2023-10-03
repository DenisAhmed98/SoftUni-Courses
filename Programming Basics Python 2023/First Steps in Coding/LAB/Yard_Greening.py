price = 7.61
discount = 0.18
area = float(input())

total_price = area*price
discount_price =total_price*discount
final_price = total_price-discount_price

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount_price} lv.")
