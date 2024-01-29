size = int(input())

matrix = [list(input()) for _ in range(size)]

knight_moves = (
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, -2),
    (2, -1),
    (1, 2),
    (2, 1)
)
removed_knights = 0

while True:
    knight_coordinates = []
    max_attacks = 0

    for rows in range(size):
        for cols in range(size):
            if matrix[rows][cols] == "K":
                can_attack = 0
                for pos in knight_moves:
                    r_pos = rows + pos[0]
                    c_pos = cols + pos[1]

                    if 0 <= r_pos < size and 0 <= c_pos < size:
                        if matrix[r_pos][c_pos] == "K":
                            can_attack += 1
                if can_attack > max_attacks:
                    max_attacks = can_attack
                    knight_coordinates = [rows, cols]

    if knight_coordinates:
        row, col = knight_coordinates
        matrix[row][col] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)