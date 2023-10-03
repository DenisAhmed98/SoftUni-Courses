type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
price_per_flower = 0
if type_of_flowers == "Roses":
    price_per_flower = 5
    if number_of_flowers > 80:
        price_per_flower *= 0.9
elif type_of_flowers == "Dahlias":
    price_per_flower = 3.80
    if number_of_flowers > 90:
        price_per_flower *= 0.85
elif type_of_flowers == "Tulips":
    price_per_flower = 2.8
    if number_of_flowers > 80:
        price_per_flower *= 0.85
elif type_of_flowers == "Narcissus":
    price_per_flower = 3
    if number_of_flowers < 120:
        price_per_flower *= 1.15
elif type_of_flowers == "Gladiolus": #else:
    price_per_flower = 2.5
    if number_of_flowers < 80:
        price_per_flower *= 1.2
total_sum = price_per_flower * number_of_flowers
difference = abs(total_sum - budget)
if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")