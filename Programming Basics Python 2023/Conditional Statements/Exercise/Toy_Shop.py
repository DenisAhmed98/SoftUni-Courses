vacation = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input()) 
number_trucks = int(input()) 
discount = 0

total_toys = number_bears+number_dolls+number_puzzles+number_minions+number_trucks
total_money_earned = number_puzzles * 2.6 + number_dolls * 3 + number_bears * 4.1 + number_minions * 8.2 + number_trucks * 2

if total_toys >= 50:
    discount = total_money_earned * 0.25

rent = (total_money_earned - discount)* 0.1

final_price = total_money_earned - rent - discount

if final_price >= vacation:
    print (f"Yes! {'%.2f' %(final_price-vacation)} lv left.")
else:
   
    print (f" Not enough money! {'%.2f' %(vacation-final_price)} lv needed.")