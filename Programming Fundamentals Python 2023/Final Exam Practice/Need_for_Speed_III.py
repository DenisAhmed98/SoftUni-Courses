def add_car(name, mileage, fuel):
    return {'name': name, 'mileage': mileage, 'fuel': fuel}


def drive_car(car, distance,fuel_req):
    if car["fuel"] >= fuel_req:
        car["mileage"] += distance
        car["fuel"] -= fuel_req
        print(f"{car['name']} driven for {distance} kilometers. {fuel_req} liters of fuel consumed.")

        if car["mileage"] >= 100000:
            print(f"Time to sell the {car['name']}!")
            return True

    else:
        print("Not enough fuel to make that ride")


def revert_mileage(car, km):
    car['mileage'] -= km
    if car['mileage'] >= 10000:
        print(f"{car['name']} mileage decreased by {km} kilometers")
    else:
        car['mileage'] = 10000


def refill_car(car,refill):
    had_fuel = car['fuel']
    car['fuel'] += refill
    if car['fuel'] > 75:
        car['fuel'] = 75
    refueled = car['fuel'] - had_fuel
    print(f"{car['name']} refueled with {refueled} liters")


vehicles = []
count = int(input())

for n in range(count):
    obtained_car = input().split("|")
    car = add_car(obtained_car[0],int(obtained_car[1]), int(obtained_car[2]))
    vehicles.append(car)

while True:
    command = input()

    if command == "Stop":
        for car in vehicles:
            print(f"{car['name']} -> Mileage: {car['mileage']} kms, Fuel in the tank: {car['fuel']} lt.")
        break

    token = command.split(" : ")
    car_name = token[1]
    action = token[0]

    for car in vehicles:
        if car["name"] == car_name:
            if action == "Drive":
                distance = int(token[2])
                fuel = int(token[3])
                if drive_car(car,distance,fuel):
                    vehicles.remove(car)

            elif action == "Refuel":
                refill = int(token[2])
                refill_car(car, refill)

            elif action == "Revert":
                km = int(token[2])
                revert_mileage(car, km)




