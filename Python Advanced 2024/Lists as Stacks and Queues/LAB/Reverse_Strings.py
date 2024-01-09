string = list(input())
reversed = []

for n in range(len(string)):
    reversed.append(string.pop())

print("".join(reversed))