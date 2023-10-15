items = input().split("|")
budget = float(input())
ticket = 0.00
profit = 0.00
bought = []

for x in items:
    temp = x.split("->")
    if temp[0] == "Clothes" and float(temp[1]) > 50.00:
        continue
    elif temp[0] == "Shoes" and float(temp[1]) > 35.00:
        continue
    elif temp[0] == "Accessories" and float(temp[1]) > 20.50:
        continue
    else:
        if budget >= float(temp[1]):
            budget -= float(temp[1])
            profit = profit + (float(temp[1]) * 0.4)
            value = float(temp[1]) + (float(temp[1]) * 0.4)
            bought.append(f"{value:.2f}")
            ticket = ticket + float(temp[1]) + (float(temp[1]) * 0.4)

print(" ".join(bought))

print(f"Profit: {profit:.2f}")

if round(ticket+budget,2) >= 150.00:
    print("Hello, France!")
else:
    print("Not enough money.")