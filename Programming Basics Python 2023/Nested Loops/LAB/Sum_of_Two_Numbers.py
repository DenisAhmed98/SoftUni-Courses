start = int(input())
end = int(input())
magic = int(input())
combinations = 0
found = False
for a in range (start,end+1):
    for b in range (start,end+1):
        combinations +=1
        if a+b == magic:
            found = True
            print(f"Combination N:{combinations} ({a} + {b} = {magic})")
            break
    if found == True:
        break

if found == False:
    print(f"{combinations} combinations - neither equals {magic}")