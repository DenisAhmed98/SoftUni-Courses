deposit_money = float(input())
deposit_time = int(input())
deposit_procent = float(input())
procent = deposit_procent/100

summ = deposit_money + deposit_time*((deposit_money*procent)/12)
print(summ)