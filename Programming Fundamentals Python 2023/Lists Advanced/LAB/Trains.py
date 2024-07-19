length_of_train = int(input())
train = [0] * length_of_train
command = input()

while command != "End":
    token = command.split(" ")
    key = token[0]
    if key == "add":
        index = int(train[-1])
        value = int(token[1])
        train[-1] = value+index
    elif key == "insert":
        train[int(token[1])] = train[int(token[1])] + int(token[2])
    elif key == "leave":
        train[int(token[1])] = train[int(token[1])] - int(token[2])

    command = input()

print(train)






