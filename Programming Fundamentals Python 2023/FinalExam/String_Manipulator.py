my_string = input()

while True:
    command = input()

    if command == "End":
        break

    token = command.split(" ")

    if token[0] == "Translate":
        my_string = my_string.replace(token[1], token[2])
        print(my_string)
    elif token[0] == "Includes":
        if token[1] in my_string:
            print("True")
        else:
            print("False")
    elif token[0] == "Start":
        start = token[1]
        match = my_string[:len(start)]
        if start == match:
            print("True")
        else:
            print("False")
    elif token[0] == "Lowercase":
        my_string = my_string.lower()
        print(my_string)
    elif token[0] == "FindIndex":
        index = 0
        for o in range(len(my_string)):
            if token[1] == my_string[o]:
                index = o
        print(index)
    elif token[0] == "Remove":
        start = int(token[1])
        end = int(token[2])
        my_string = my_string[:start] + my_string[end+start:]
        print(my_string)