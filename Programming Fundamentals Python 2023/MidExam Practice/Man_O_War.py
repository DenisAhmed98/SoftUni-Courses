pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
maximum_health_of_section = int(input())
while True:
    command_list = input().split(" ")
    if command_list[0] == "Retire":
        sum_pirate = 0
        sum_warship = 0
        for s in pirate_ship_status:
            sum_pirate += int(s)
        for w in warship_status:
            sum_warship += int(w)

        print(f"Pirate ship status: {sum_pirate}")
        print(f"Warship status: {sum_warship}")
        break

    if command_list[0] == "Fire":
        index = int(command_list[1])
        damage = int(command_list[2])
        if index < len(warship_status)+1:
            health = warship_status[index]
            health -= damage
            if health <= 0:
                print("You won! The enemy ship has sunken.")
                break
            else:
                warship_status[index] = health
        else:
            continue
    if command_list[0] == "Defend":
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        damage = int(command_list[3])
        flag = 0
        if start_index < len(pirate_ship_status)+1 and end_index <= len(pirate_ship_status)+1:
            for hit in range(start_index,end_index):
                health = pirate_ship_status[hit]
                health -= damage
                if health <= 0:
                    print("You lost! The pirate ship has sunken.")
                    flag = 1
                    break
                else:
                    pirate_ship_status[hit] = health
            if flag == 1:
                break
        else:
            continue

    if command_list[0] == "Repair":
        index = int(command_list[1])
        health = int(command_list[2])
        if index <= len(pirate_ship_status):
            healed = pirate_ship_status[index]
            healed += health
            if healed > maximum_health_of_section:
                healed = maximum_health_of_section
            pirate_ship_status[index] = healed
        else:
            continue

    if command_list[0] == "Status":
        count = 0
        for section in pirate_ship_status:
            percent = maximum_health_of_section * 0.2
            if int(section) < percent:
                count += 1
        print(f"{count} sections need repair.")

