budget = float(input())
flour = float(input())
eggs = flour * 0.75
milk = flour + (flour * 0.25)
money_left = budget
breadcount = 0
eggs_count = 0
counter = 0
loaf = flour + eggs + (milk * 0.25)
while money_left > loaf:
    money_left -= loaf
    eggs_count += 3
    breadcount +=1
    counter +=1
    if counter == 3:
        eggs_count = eggs_count - (breadcount - 2)
        counter = 0

    loaf = flour + eggs + (milk * 0.25)
print(f"You made {breadcount} loaves of Easter bread! Now you have {eggs_count} eggs and {money_left:.2f}BGN left.")

