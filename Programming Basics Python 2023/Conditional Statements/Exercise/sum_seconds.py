number = int(input())
bonus = 0

if number <=100:
    bonus = 5
elif number>100 and number < 1000:
    bonus = number*0.2
else:
    bonus = number*0.1

if number%2 == 0:
    bonus = bonus+1

if number%10 == 5:
    bonus = bonus+2
    print (number/10)

print (bonus)
print (number+bonus)