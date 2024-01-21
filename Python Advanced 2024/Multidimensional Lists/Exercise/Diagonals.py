size = int(input())
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split(", ")))
    for y in range(0, size):
        matrix[x][y] = line[y]

primary = []
secondary = []
for i in range (size):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][size-i-1])

print(f"Primary diagonal: {', '.join([f'{g}' for g in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([f'{g}' for g in secondary])}. Sum: {sum(secondary)}")