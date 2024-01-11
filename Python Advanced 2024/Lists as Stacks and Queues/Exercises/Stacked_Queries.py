cycle = int(input())
stack = []


for c in range(cycle):
    query = input().split()
    if int(query[0]) == 1:
        stack.append(int(query[1]))
    if int(query[0]) == 2:
        if stack:
            stack.pop()
    if int(query[0]) == 3:
        if stack:
            print(max(stack))
    if int(query[0]) == 4:
        if stack:
            print(min(stack))

for n in range(len(stack)-1):
    print(stack.pop(), end=", ")
print(stack.pop())
#print(",".join(map(str, stack)))
