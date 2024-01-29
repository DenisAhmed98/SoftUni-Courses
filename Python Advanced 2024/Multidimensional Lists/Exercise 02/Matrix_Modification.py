size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input().split()

while command[0] != "END":
    operation, x, y, number = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= x < size and  0 <= y < size):
        print("Invalid coordinates")
    else:
        if operation == "Add":
            matrix[x][y] += number
        elif operation == "Subtract":
            matrix[x][y] -= number

    command = input().split()

[print(*row) for row in matrix]