from collections import deque

fuel = list(map(int, input().split()))
consumption = deque(list(map(int, input().split())))
required_fuel = deque(list(map(int, input().split())))
alt_length = len(fuel)
altitude = 0
list_alt = []
while True:
    if not fuel:
        break
    fuel_consumption = fuel[-1] - consumption[0]
    needed_fuel = required_fuel.popleft()
    fuel.pop()
    consumption.popleft()
    if fuel_consumption >= needed_fuel:
        altitude += 1
        list_alt.append(f"Altitude {altitude}")
        print(f"John has reached: Altitude {altitude}")
    else:
        print(f"John did not reach: Altitude {altitude + 1}")
        break
if altitude == alt_length:
    print(f"John has reached all the altitudes and managed to reach the top!")
elif altitude == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
elif 0 < altitude < alt_length:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(str(x) for x in list_alt)}")
        

