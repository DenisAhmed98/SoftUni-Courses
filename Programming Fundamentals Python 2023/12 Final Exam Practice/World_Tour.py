stops = input()

while True:
    command = input()

    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    token = command.split(":")
    if token[0] == "Add Stop":
        index = int(token[1])
        string = token[2]
        stops = stops[:index] + string + stops[index:]
        print(stops)
    elif token[0] == "Remove Stop":
        start = int(token[1])
        end = int(token[2])
        if start in range(len(stops)) and end in range(len(stops)):
            stops = stops[:start] + stops[end+1:]
        print(stops)
    elif token[0] == "Switch":
        old = token[1]
        new = token[2]
        if old in stops:
            stops = stops.replace(old, new)
        print(stops)
