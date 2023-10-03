hours = int(input())
minutes = int(input())

minutes = minutes+15 

if minutes > 59:
    hours = hours + 1
    minutes = minutes - 60

if hours > 23:
    hours = hours - 24

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
