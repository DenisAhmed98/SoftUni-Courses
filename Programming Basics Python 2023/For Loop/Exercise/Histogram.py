numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range (numbers):
    num_sequeance = int(input())
    if num_sequeance < 200:
        p1 +=1
    elif 200 <= num_sequeance < 400:
        p2 +=1
    elif 400 <= num_sequeance < 600:
        p3 +=1
    elif 600 <= num_sequeance < 800:
        p4 +=1
    elif num_sequeance >= 800:
        p5 +=1

print(f"{p1/numbers*100:.2f}%")
print(f"{p2/numbers*100:.2f}%")
print(f"{p3/numbers*100:.2f}%")
print(f"{p4/numbers*100:.2f}%")
print(f"{p5/numbers*100:.2f}%")