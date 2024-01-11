from collections import deque

qunatity_of_food = int(input())

orders = deque(map(int, input().split()))

print(max(orders))
while orders:
    if orders[0] <= qunatity_of_food:
        qunatity_of_food -= orders[0]
        orders.popleft()
    else:
        break


left = " ".join(map(str, orders))

if orders:
    print(f"Orders left: {left}")
else:
    print("Orders complete")

