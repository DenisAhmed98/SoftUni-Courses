numbers = list(map(int, input().split(" ")))

while True:
    command = input().split(" ")
    if command[0] == "Finish":
        break
    elif command[0] == "Add":
        numbers.append(int(command[1]))
    elif command[0] == "Remove":
        for i in range(len(numbers)):
            if numbers[i] == int(command[1]):
                numbers.pop(i)
                break
    elif command[0] == "Replace":
        for i in range(len(numbers)):
            if numbers[i] == int(command[1]):
                numbers[i] = int(command[2])
                break
    elif command[0] == "Collapse":
        numbers = list(filter(lambda x: x >= int(command[1]), numbers))

print(f"{' '.join(str(x) for x in numbers)}")