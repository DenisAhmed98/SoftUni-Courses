rows = int(input())
matrix = []

for i in range(rows):
    row = input().split(", ")
    matrix.append(list(map(int, row)))


flattened = [num for sublist in matrix for num in sublist]
print(flattened)