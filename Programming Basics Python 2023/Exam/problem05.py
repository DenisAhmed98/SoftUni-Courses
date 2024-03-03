target = int(input())
money = 0
client = input()

while client != "closed":
    if client == "haircut":
        client= input()
        if client == "mens":
            money +=15
        elif client == "ladies":
            money += 20
        elif client == "kids":
            money += 10

        if money>=target:
            break

    elif client == "color":
        client = input()
        if client == "touch up":
            money += 20
        elif client == "full color":
            money += 30
        if money>=target:
            break

    client = input()

if money>=target:
    print(f"You have reached your target for the day!")
else:
    print(f"Target not reached! You need {target-money}lv. more.")

print(f"Earned money: {money}lv.")
