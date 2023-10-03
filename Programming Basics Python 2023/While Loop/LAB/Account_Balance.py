balance = 0
while True:
    money = input()
    if money == "NoMoreMoney":
        break
    else:
        money = float(money)
    if money < 0:
        print("Invalid operation!")
        break
    else:
        balance += money
        print(f"Increase: {money:.2f}")
print(f"Total: {balance:.2f}")