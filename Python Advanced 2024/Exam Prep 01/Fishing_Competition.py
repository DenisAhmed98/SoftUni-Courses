fishing_area = int(input())
matrix = []
ship_position = []
cought_fish = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(fishing_area):
    matrix.append(list(input()))

    if 'S' in matrix[row]:
        ship_position = [row, matrix[row].index('S')]

command = input()
while command != "collect the nets":
    p_row,p_col = ship_position
    row = ship_position[0] + directions[command][0]
    col = ship_position[1] + directions[command][1]

    if row < 0:
        row = fishing_area - 1
    if row > fishing_area - 1:
        row = 0
    if col < 0:
        col = fishing_area - 1
    if col > fishing_area - 1:
        col = 0
    ship_position = row, col
    symbol = matrix[row][col]
    if symbol.isdigit():
        cought_fish += int(matrix[row][col])
        matrix[p_row][p_col] = "-"
        matrix[row][col] = "S"
    elif matrix[row][col] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row},{col}]")
        exit()
    else:
        matrix[p_row][p_col] = "-"
        matrix[row][col] = "S"

    command = input()

if cought_fish >= 20:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - cought_fish} tons of fish more.")

if cought_fish:
    print(f"Amount of fish caught: {cought_fish} tons.")

print(*[''.join(row) for row in matrix], sep='\n')
