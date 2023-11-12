number_commands = int(input())
register = {}

for num in range(number_commands):
    command = input().split(" ")
    if command[0] == "register":
        username = command[1]
        license_plate = command[2]
        if username not in register.keys():
            register[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {register[username]}")
    elif command[0] == "unregister":
        username = command[1]
        if username not in register.keys():
            print(f"ERROR: user {username} not found")
        else:
            register.pop(username)
            print(f"{username} unregistered successfully")

for key, value in register.items():
    print(f"{key} => {value}")

