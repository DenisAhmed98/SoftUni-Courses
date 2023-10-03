from math import floor
tournaments = int(input())
starting_points = int(input())
avg_points = 0
won = 0
for i in range(tournaments):
    char = input()
    
    if char == "W":
        avg_points +=2000
        won +=1
    elif char == "F":
        avg_points +=1200
    elif char == "SF":
        avg_points +=720

print(f"Final points: {starting_points+avg_points}")
print(f"Average points: {floor(avg_points/tournaments)}")
print(f"{won/tournaments*100:.2f}%")