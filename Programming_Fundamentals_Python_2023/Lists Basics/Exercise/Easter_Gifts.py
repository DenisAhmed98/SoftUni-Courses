items = [x for x in input().split()]
values_input = input().split()
outofstocklist = []
required = []
justincase = []

if values_input[0] == "OutOfStock":
    outofstocklist.append(values_input[1])
elif values_input[0] == "Required":
    required.append(values_input[1])
    required.append(values_input[2])
elif values_input[0] == "JustInCase":
    justincase.append(values_input[1])

while values_input != "No Money":
    if values_input[0] == "OutOfStock":
        outofstocklist.append(values_input[1])
    elif values_input[0] == "Required":
        required.append(values_input[1])
        required.append(values_input[2])
    elif values_input[0] == "JustInCase":
        justincase.append(values_input[1])

counter = 0
for x in items:
    if counter ==


print(items)
