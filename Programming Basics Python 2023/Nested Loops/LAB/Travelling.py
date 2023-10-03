while True:
    city = input()
    if city == "End":
        break
    money = 0
    budget = float(input())
    while money < budget:
        invest = float(input())
        money += invest
    print(f"Going to {city}!")