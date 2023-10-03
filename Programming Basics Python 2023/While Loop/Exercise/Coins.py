money = float(input())
money = int(money*100)
counter = 0
counter += money // 200
money = money % 200
counter += money // 100
money = money % 100
counter += money // 50
money = money % 50
counter += money // 20
money = money % 20
counter += money // 10
money = money % 10
counter += money // 5
money = money % 5
counter += money // 2
money = money % 2
counter += money // 1
money = money % 1

print(counter)