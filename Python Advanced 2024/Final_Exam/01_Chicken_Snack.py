from collections import deque

change = list(map(int, input().split()))
prices = deque(list(map(int, input().split())))
eaten_food = 0

while change and prices:
    current_change = change[-1]
    current_price = prices[0]
    if current_change == current_price:
        eaten_food +=1
        change.pop()
        prices.popleft()
    elif current_change > current_price:
        change.pop()
        prices.popleft()
        if change:
            money_left = current_change - current_price
            change[-1] += money_left
        eaten_food +=1
    else:
        change.pop()
        prices.popleft()

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif 1 < eaten_food < 4:
    print(f"Henry ate: {eaten_food} foods.")
elif eaten_food == 1:
    print(f"Henry ate: {eaten_food} food.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")