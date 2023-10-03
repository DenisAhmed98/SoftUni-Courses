length = int(input())
width = int(input())
height = int(input())
procent = float(input())/100

aquarium_size = length*width*height
aquarium_liters = aquarium_size*0.001
needed_liters = aquarium_liters*(1-procent)

print(needed_liters)