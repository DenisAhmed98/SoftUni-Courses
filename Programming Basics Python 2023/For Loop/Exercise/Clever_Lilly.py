age = int(input())
washing_machine = float(input())
toy = int(input())
money = 0
increment = 1
for i in range (1,age+1):
    if i%2==0:
        money = money + (10*increment)-1
        increment +=1
    else:
        money = money + toy
if money>=washing_machine:
    print(f"Yes! {money-washing_machine:.2f}")
else:
    print(f"No! {washing_machine-money:.2f}")

