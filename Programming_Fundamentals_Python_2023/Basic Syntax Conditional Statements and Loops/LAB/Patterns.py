stars = int(input())

for i in range (stars):
    for j in range(i+1):
        print("*", end="")
    print()

for i in range (stars-1,0,-1):
    for j in range(i):
        print("*", end="")
    print()