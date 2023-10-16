numbers = input().split(" ")
string = [x for x in input()]
message = ""
for x in numbers:
    temp = [n for n in x]
    num = 0
    for var in temp:
        num += int(var)

    while len(string) < num:
        num -= len(string)

    message += string[num]
    string.pop(num)

print(message)


