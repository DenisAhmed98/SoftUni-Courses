string = list(map(int, input().split()))

for n in range(len(string)):
    print(string.pop(), end=" ")
