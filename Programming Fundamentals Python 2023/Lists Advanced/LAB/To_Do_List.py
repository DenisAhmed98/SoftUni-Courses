notes = [0] * 10


while True:
    command = input()
    if command == "End":
        break
    token = command.split("-")
    priority = int(token[0])-1
    note = token[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [elements for elements in notes if elements != 0]
print(result)






