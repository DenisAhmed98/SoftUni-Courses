from collections import deque

names = deque(input().split())
potato = int(input()) - 1

while len(names) > 1:
    names.rotate(-potato)
    lost = names.popleft()
    print(f"Removed {lost}")

print(f"Last is {names.popleft()}")