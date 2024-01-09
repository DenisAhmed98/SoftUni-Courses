from collections import deque

people = deque([])

while True:
    command = input()
    if command == "End":
        print(f"{len(people)} people remaining.")
        break
    elif command == "Paid":
        for person in range(len(people)):
            print(people.popleft())
    else:
        people.append(command)


