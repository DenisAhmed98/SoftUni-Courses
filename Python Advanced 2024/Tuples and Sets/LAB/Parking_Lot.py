commands_number = int(input())
cars = set()

for c in range(commands_number):
    command = input().split(", ")
    direction, car_number = command

    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)

if cars:
    for c in cars:
        print(c)
else:
    print("Parking Lot is Empty")
