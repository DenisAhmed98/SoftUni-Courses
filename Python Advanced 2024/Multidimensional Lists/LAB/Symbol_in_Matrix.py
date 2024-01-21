size = int(input())
matrix_of_chars = []

for _ in range(0, size):
    matrix_of_chars.append(list(input()))

symbol = input()
location = ()
found = False

for row in range(0, size):
    if found:
        break
    for col in range(0, size):
        if matrix_of_chars[row][col] == symbol:
            location = (row, col)
            found = True

if found:
 print(location)
else:
 print(f"{symbol} does not occur in the matrix")