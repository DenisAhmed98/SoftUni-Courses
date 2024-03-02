size = int(input())

matrix = []
jet_position = []
armor = 300
enemies = 0

for row in range(size):
    matrix.append(list(input()))
    if "J" in matrix[row]:
        jet_position = [row, matrix[row].index("J")]
    if "E" in matrix[row]:
        enemies += matrix[row].count("E")

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()
    prev_row, prev_col = jet_position[0], jet_position[1]
    row = jet_position[0] + directions[command][0]
    col = jet_position[1] + directions[command][1]

    if matrix[row][col] == "R":
        matrix[prev_row][prev_col] = "-"
        matrix[row][col] = "J"
        jet_position = row,col
        armor = 300
    elif matrix[row][col] == "E":
        matrix[prev_row][prev_col] = "-"
        matrix[row][col] = "J"
        jet_position = row, col
        enemies -= 1
        if enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor -=100
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
                break
    else:
        matrix[prev_row][prev_col] = "-"
        matrix[row][col] = "J"
        jet_position = row, col


print(*[''.join(row) for row in matrix], sep='\n')