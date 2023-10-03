budget = float(input())
number_people = int(input())
price_per_clothing = float(input())
decor = budget * 0.1

price = number_people * price_per_clothing
discount = 0

if number_people>150:
    discount = price * 0.1

total = price - discount + decor

if budget >= total:
    print ("Action!")
    print (f"Wingard starts filming with {'%.2f'%(budget-total)} leva left.")
else:
    print ("Not enough money!")
    print (f"Wingard needs {'%.2f'%(total-budget)} leva more.")