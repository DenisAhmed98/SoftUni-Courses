def decypher (list, message):
    for command in list:
        token = command.split("|")
        if token[0] == "Move":
            number = int(token[1])
            message = message[number:] + message[:number]
        if token[0] == "Insert":
            index = int(token[1])
            value = token[2]
            message = message[:index] + value + message[index:]
        if token[0] == "ChangeAll":
            substring = token[1]
            replacement = token[2]
            message = message.replace(substring, replacement)
    return message


encrypted_message = input()
command_list = []

while True:
    command = input()
    if command == "Decode":
        break

    command_list.append(command)

print(f"The decrypted message is: {decypher(command_list, encrypted_message)}")