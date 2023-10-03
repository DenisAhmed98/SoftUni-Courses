from sys import maxsize
smallest = maxsize

while True:
    num = input()
    if num == "Stop":
        break
    else:
        num = int(num)
    if smallest > num:
        smallest = num

print(smallest)