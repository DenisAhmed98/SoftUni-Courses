rows, cols = [int(x) for x in input().split(", ")]
matrix = []
matrix_Sum = 0
for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix_Sum += sum(lines)
    matrix.append(lines)

print(matrix_Sum)
print(matrix)