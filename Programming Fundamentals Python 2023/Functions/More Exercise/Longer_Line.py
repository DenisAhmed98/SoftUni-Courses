import math
def checkLine(x1,y1,x2,y2):
    line = math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))
    return line

def pointsDistance(x1,y1,x2,y2):
    distanceA = math.hypot(0-y1,0-x1)
    distanceB = math.hypot(0-y2,0-x2)
    distanceA = int(math.floor(distanceA))
    distanceB = int(math.floor(distanceB))
    if distanceA > distanceB:
        print(f"({int(math.floor(x2))}, {int(math.floor(y2))})({int(math.floor(x1))}, {int(math.floor(y1))})")
    else:
        print(f"({int(math.floor(x1))}, {int(math.floor(y1))})({int(math.floor(x2))}, {int(math.floor(y2))})")

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

lineA = checkLine(x1,y1,x2,y2)
lineB = checkLine(x3,y3,x4,y4)

if lineA >= lineB:
    pointsDistance(x1,y1,x2,y2)
else:
    pointsDistance(x3,y3,x4,y4)