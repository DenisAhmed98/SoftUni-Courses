budget = float(input())
num_GPU = int(input())
num_CPU = int(input())
num_RAM = int(input())

discount = 0
price = num_GPU*250
cpu = num_CPU*(price * 0.35)
ram = num_RAM*(price * 0.1)
total = price + cpu + ram
if num_GPU>num_CPU:
    discount = total * 0.15
total -= discount

if budget>=total:
    print(f"You have {'%.2f'%(budget-total)} leva left!")
if budget<total:
    print(f"Not enough money! You need {'%.2f' % (total-budget)} leva more!")

