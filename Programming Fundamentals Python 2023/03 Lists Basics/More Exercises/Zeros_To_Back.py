numbers = input().split(", ")
result = []
counter = 0

for x in numbers:
    if int(x) != 0:
        result.append(int(x))
    else:
        counter +=1
for y in range(counter):
    result.append(0)

print(result)
