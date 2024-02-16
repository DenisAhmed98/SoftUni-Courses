size = int(input())
money = 100
gabler_position = []
matrix = []

for row in range(size):
    matrix.append(list(input()))
    if "G" in matrix[row]:
        gabler_position = [row, matrix[row].index("G")]

directions = {  # създаваме променлива, в която да пазим посоките
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while command != "end":
    p_row, p_col = gabler_position[0],gabler_position[1]

    row = gabler_position[0] + directions[command][0]
    col = gabler_position[1] + directions[command][1]

    if row < 0 or col < 0:
        break
    if row > size -1 or col > size -1:
        break 
    
    if matrix[row][col] == "W":
        money += 100
        matrix[p_row][p_col] = "-"
        matrix[row][col] = "G"
        gabler_position = row,col

    elif matrix[row][col] == "P":
        money -= 200
        if money <= 0:
            print("Game over! You lost everything!")
            exit()
        else:
            matrix[p_row][p_col] = "-"
            matrix[row][col] = "G"
            gabler_position = row,col 
    elif matrix[row][col] == "J":
        money += 100000
        matrix[p_row][p_col] = "-"
        matrix[row][col] = "G"
        gabler_position = row,col
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {money}$")
        print(*[''.join(row) for row in matrix], sep='\n')
        exit()
    else:
        matrix[p_row][p_col] = "-"
        matrix[row][col] = "G"
        gabler_position = row,col

    command = input()

print(f"End of the game. Total amount: {money}$")
print(*[''.join(row) for row in matrix], sep='\n')