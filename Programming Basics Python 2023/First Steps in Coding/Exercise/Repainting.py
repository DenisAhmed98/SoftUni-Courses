naylon = 1.50
paint = 14.50
paint_chemical = 5.00

naylon_needed = int(input())+2
paint_needed = int(input())
chemical_needed = int(input())
working_time = int(input())

aditional_paint = paint_needed*0.1

naylon_price = naylon_needed*naylon
paint_price = paint*(paint_needed+aditional_paint)
chemical_price = chemical_needed*paint_chemical
bag_price = 0.40

total_price = naylon_price+paint_price+chemical_price+bag_price

painter_price = (total_price*0.3)*working_time

final_price = total_price+painter_price

print(final_price)