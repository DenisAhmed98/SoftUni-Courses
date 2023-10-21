#time: 23min
player_health = 100
player_coins = 0
room_counter = 1
dungeon = input().split("|")

for room in dungeon:
    command, amount = room.split(" ")
    if command == "potion":
        healed = 0
        if player_health < 100:
            player_health += int(amount)
            healed = int(amount)
            if player_health > 100:
                healed = int(amount) - (player_health-100)
                player_health = 100
        print(f"You healed for {healed} hp.")
        print(f"Current health: {player_health} hp.")
    elif command == "chest":
        player_coins += int(amount)
        print(f"You found {amount} bitcoins.")
    else:
        attack = int(amount)
        player_health -= attack
        if player_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            break
    if room_counter == len(dungeon):
        print("You've made it!")
        print(f"Bitcoins: {player_coins}")
        print(f"Health: {player_health}")
    room_counter += 1
