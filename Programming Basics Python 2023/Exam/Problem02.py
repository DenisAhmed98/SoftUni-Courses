price_for_party = float(input())
love_letters_count = int(input())
price = love_letters_count*0.60
roses_count = int(input())
price = price + roses_count*7.20
keychains_count = int(input())
price = price + keychains_count*3.60
paintings_count = int(input())
price = price + paintings_count*18.20
lucks_count = int(input())
price = price +lucks_count*22
discount = 0
total_count = love_letters_count + roses_count + keychains_count + paintings_count + lucks_count

if total_count >= 25:
    discount = price*0.35
    price -= discount

hosting = price*0.1
price -= hosting

if price >= price_for_party:
    print(f"Yes! {price-price_for_party:.2f} lv left.")
else:
    print(f"Not enough money! {price_for_party-price:.2f} lv needed.")
