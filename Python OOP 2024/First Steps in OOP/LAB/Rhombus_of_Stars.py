count = int(input())

def printRows(stars,count):
    for row in range(count-stars):
        print(" ", end="")
    for row in range(1, stars):
        print("*",end=" ")
    print("*")


for stars in range(1, count):
    printRows(stars,count)
for stars in range(count,0,-1):
    printRows(stars,count)