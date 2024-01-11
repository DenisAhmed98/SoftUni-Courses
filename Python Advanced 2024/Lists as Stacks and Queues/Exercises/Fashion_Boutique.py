box_of_clothes = map(int, input().split())
rack_capacity = int(input())
racks = []
rack = 0

for n in box_of_clothes:
    if n <= rack_capacity:
        if racks:
            if racks[-1]+n > rack_capacity:
                racks.append(n)
            else:
                racks[-1] += n
        else:
            racks.append(n)

print(len(racks))