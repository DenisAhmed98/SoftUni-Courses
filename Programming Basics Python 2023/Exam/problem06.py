number = int(input())
f1 = int(number%10)
number = number / 10
f2 = int(number%10)
number = number / 10
f3 = int(number%10)

for i in range (1,f1+1):
    for b in range(1,f2+1):
        for c in range(1,f3+1):
            print(f"{i} * {b} * {c} = {i*b*c};")