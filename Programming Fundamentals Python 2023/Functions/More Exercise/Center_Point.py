import math

def pointsDistance(x1,y1,x2,y2):
    distanceA = math.hypot(0-y1,0-x1)
    distanceB = math.hypot(0-y2,0-x2)
    distanceA = int(math.floor(distanceA))
    distanceB = int(math.floor(distanceB))
    if distanceA > distanceB:
        print(f"({int(math.floor(x2))}, {int(math.floor(y2))})")
    else:
        print(f"({int(math.floor(x1))}, {int(math.floor(y1))})")

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

pointsDistance(x1,y1,x2,y2)