from collections import deque

pumps_data = deque([int(x) for x in input().split()] for _ in range(int(input())))

data_copy = pumps_data.copy()
gas_fill = 0
pump_number = 0
while data_copy:
    gas, distance = data_copy.popleft()
    gas_fill += gas

    if gas_fill >= distance:
        gas_fill -= distance
    else:
        pumps_data.rotate(-1)
        data_copy = pumps_data.copy()
        pump_number += 1
        gas_fill = 0

print(pump_number)