num = int (input())
sum = 0
for x in range (0, num+1):
    for y in range (0, num+1):
        for z in range (0, num+1):
            if x+y+z == num:
                sum +=1
print(sum)