dancers = int(input())
points = float(input())
season = input()
place = input()
price = 0
charity = 0

price = dancers * points

if place == "Abroad":
    price = price + (price * 0.5)

if place == "Bulgaria" and season == "summer":
    price = price - (price*0.05)

elif place == "Bulgaria" and season == "winter":
    price = price - (price*0.08)
elif place == "Abroad" and season == "summer":
    price = price - (price*0.1)
elif place == "Abroad" and season == "winter":
    price = price - (price*0.15)

charity = price * 0.75
price = price - charity

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {price/dancers:.2f}")