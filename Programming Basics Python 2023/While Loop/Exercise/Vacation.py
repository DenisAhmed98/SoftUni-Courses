money_needed = float(input())
starting_money = float(input())
days = 0
spend = 0

while starting_money < money_needed and spend < 5:
    command = input()
    money = float(input())
    days+=1
    if command == "save":
        starting_money +=money
        spend = 0
    elif command == "spend":
        starting_money -=money
        spend +=1
        if starting_money <0:
            starting_money = 0

if spend == 5:
    print("You can't save the money.")
    print(days)
if starting_money >= money_needed:
    print(f"You saved the money for {days} days.")