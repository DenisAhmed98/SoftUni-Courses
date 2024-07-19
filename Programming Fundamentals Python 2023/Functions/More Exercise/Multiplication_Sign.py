def checker(numA,numB,numC):
    flag = 0
    if numA < 0:
        flag +=1
    if numB < 0:
        flag +=1
    if numC < 0:
        flag +=1
    if numA == 0 or numB == 0 or numC == 0:
        return "zero"
    elif flag % 2 == 1 :
        return "negative"
    else:
        return "positive"

numA = int(input())
numB = int(input())
numC = int(input())

print(checker(numA,numB,numC))