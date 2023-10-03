from sys import maxsize
bigest = -maxsize

while True:
    num = input()
    if num == "Stop":
        break
    else:
        num = int(num)
    if bigest < num:
        bigest = num

print(bigest)