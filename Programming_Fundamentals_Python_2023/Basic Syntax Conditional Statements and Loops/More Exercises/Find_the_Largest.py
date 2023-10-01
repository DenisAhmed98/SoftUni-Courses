number = input()
newnum = []
output = ""
for i in number:
    newnum.append(int(i))

newnum.sort(reverse=True)
for i in newnum:
    output +=str(i)

print(output)

