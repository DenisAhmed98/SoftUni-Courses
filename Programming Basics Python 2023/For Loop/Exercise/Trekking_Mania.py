group_Count = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
ktwo = 0
everest = 0
total = 0

for i in range (group_Count):
    people  = int(input())
    total += people

    if people <= 5:
        musala +=people
    elif 6 <= people <= 12:
        monblan +=people
    elif 13 <= people <= 25:
        kilimandjaro +=people
    elif 26 <= people <= 40:
        ktwo +=people
    elif people >= 41:
        everest +=people
print (f"{musala/total*100:.2f}%")
print (f"{monblan/total*100:.2f}%")
print (f"{kilimandjaro/total*100:.2f}%")
print (f"{ktwo/total*100:.2f}%")
print (f"{everest/total*100:.2f}%")