items = [x for x in input().split()]
items_first_iter = []
items_second_iter = []
items_third_iter = []
outofstocklist = []
required = []
justincase = []

command = input()
for item in items:
    if command == "No Money":
        break
    for item in items:
        if "OutOfStock" in command:
            if item == command.replace("OutOfStock ",""):
                items_first_iter.append("None")
        elif "Required" in command:
            temp_commands = command.split()
            if int(temp_commands[2]) > len(items):
                break
            else:
                items_first_iter.pop(int(temp_commands[2]))
                items_first_iter.insert(int(temp_commands[2]),temp_commands[1])
                break
        elif "JustInCase" in command:
            justincase.append(command.replace("JustInCase ",""))
        else:
            items_first_iter.append(item)

# if "OutOfStock" in command:
#     outofstocklist.append(command.replace("OutOfStock ",""))
# elif "Required" in command:
#     temp_commands = command.split()
#     required.append(temp_commands[1])
#     required.append(temp_commands[2])
# elif "JustInCase" in command:
#     justincase.append(command.replace("JustInCase ",""))

while command != "No Money":
    command = input()
    if command == "No Money":
        break
    for item in items:
        if "OutOfStock" in command:
            if item == command.replace("OutOfStock ",""):
                items_first_iter.append("None")
        elif "Required" in command:
            temp_commands = command.split()
            if int(temp_commands[2]) > len(items):
                break
            else:
                items_first_iter.pop(int(temp_commands[2]))
                items_first_iter.insert(int(temp_commands[2]),temp_commands[1])
                break
        elif "JustInCase" in command:
            justincase.append(command.replace("JustInCase ",""))
        else:
            items_first_iter.append(item)

items_first_iter.pop(-1)
items_first_iter.append(justincase[0])

for x in items_first_iter:
    if x == "None":
        items_first_iter.remove("None")


joined_string = " ".join(map(str,items_first_iter))
print(joined_string, end="")







#print(items)