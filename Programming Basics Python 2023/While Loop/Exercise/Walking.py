total = 0
while True:
    steps = input()
    if steps == "Going home":
        steps = int(input())
        total += int(steps)
        break
    total += int(steps)
    if total >= 10000:
        break
if total >= 10000:
    print("Goal reached! Good job!")
    print(f"{total-10000} steps over the goal!")
else:
    print(f"{10000-total} more steps to reach goal.")