lines = int(input())
opening = 0
closing = 0
last_bracket = 0
flag = False
for characters in range (lines):

    character = input()
    for i in character:
        if i == "(":
            opening +=1
            if last_bracket == 1:
                flag = True
                break
            last_bracket = 1
        elif i == ")":
            closing +=1
            last_bracket = 0
    if flag == True:
        break

if flag == True:
    print("UNBALANCED")
elif opening != closing:
    print("UNBALANCED")
else:
    print("BALANCED")
