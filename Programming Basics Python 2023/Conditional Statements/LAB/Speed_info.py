from math import pi 

figure = input()

if figure=="square":
    side_a = float(input())
    print('%.3f' % (side_a*side_a))
if figure=="rectangle":
    side_a = float(input())
    side_b = float(input())
    print('%.3f' % (side_a*side_b))
if figure=="circle":
    radius = float(input())
    print('%.3f' % (pi*radius*radius))
if figure=="triangle":
    side_a = float(input())
    side_b = float(input())
    print('%.3f' % (side_a*side_b/2))


