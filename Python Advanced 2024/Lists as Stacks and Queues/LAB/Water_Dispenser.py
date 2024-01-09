from collections import deque

water = int(input())
people = deque()
while True:
    names = input()
    if names == "Start":
        break
    else:
        people.append(names)

while True:
    command = input().split()
    if command[0] == "End":
        print(f"{water} liters left")
        break
    elif len(command) == 1:
        if int(command[0]) <= water:
            print(f"{people.popleft()} got water")
            water -= int(command[0])
        else:
            print(f"{people.popleft()} must wait")
    elif len(command) == 2:
        refill = int(command[1])
        water += refill


