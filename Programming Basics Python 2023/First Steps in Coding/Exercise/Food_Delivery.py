chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery = 2.50

number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vegetarian_menu = int(input())

total_food_price = chicken_menu*number_of_chicken_menu + fish_menu*number_of_fish_menu + vegetarian_menu*number_of_vegetarian_menu
desert_price = total_food_price*0.2

total_price = total_food_price+desert_price+delivery

print("%.2f" % total_price)

