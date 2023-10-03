city = input()
sales = float(input())
comissions = 0

if city == "Sofia":
    if 0<= sales <= 500:
        comissions = 0.05
        print(f"{sales * comissions:.2f}")
    elif 500< sales <= 1000:
        comissions = 0.07
        print(f"{sales * comissions:.2f}")
    elif 1000 < sales <= 10000:
        comissions = 0.08
        print(f"{sales * comissions:.2f}")
    elif sales > 10000:
        comissions = 0.12
        print(f"{sales * comissions:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        comissions = 0.055
        print(f"{sales * comissions:.2f}")
    elif 500 < sales <= 1000:
        comissions = 0.08
        print(f"{sales * comissions:.2f}")
    elif 1000 < sales <= 10000:
        comissions = 0.12
        print(f"{sales * comissions:.2f}")
    elif sales > 10000:
        comissions = 0.145
        print(f"{sales * comissions:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= sales <= 500:
        comissions = 0.045
        print(f"{sales * comissions:.2f}")
    elif 500 < sales <= 1000:
        comissions = 0.075
        print(f"{sales * comissions:.2f}")
    elif 1000 < sales <= 10000:
        comissions = 0.1
        print(f"{sales * comissions:.2f}")
    elif sales > 10000:
        comissions = 0.13
        print(f"{sales * comissions:.2f}")
    else:
        print("error")
else:
    print("error")