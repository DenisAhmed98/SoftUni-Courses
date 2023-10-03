annual_tax = float(input())

basketball_shoes = annual_tax - (annual_tax*0.4)
basketball_clothes = basketball_shoes - (basketball_shoes*0.2)
basketball = basketball_clothes / 4
basketball_accessories = basketball/5

total_expenses = annual_tax+basketball_shoes+basketball_clothes+basketball+basketball_accessories

print(total_expenses)