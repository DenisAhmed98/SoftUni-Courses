#finished in 27min

fires_in_cells = input().split("#")
water = int(input())

effort = 0
total_fire = 0
cells = []
for fires in fires_in_cells:
    temp = fires.split(" = ")
    if temp[0] == "High":
        if 81 <= int(temp[1]) <= 125:
            cells.append(int(temp[1]))
    elif temp[0] == "Medium":
        if 51 <= int(temp[1]) <= 80:
            cells.append(int(temp[1]))
    elif temp[0] == "Low":
        if 1 <= int(temp[1]) <= 50:
            cells.append(int(temp[1]))
print("Cells:")
for values in cells:
    if water >= values:
        water -= values
        total_fire += values
        effort = effort + (values * 0.25)
        print(f" - {values}")
    if water <= 0:
        break

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
