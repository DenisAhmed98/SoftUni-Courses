price_of_CPU_Dollar = float(input())
price_of_CPU_leva = price_of_CPU_Dollar * 1.57
price_of_Video_Dollar = float(input())
price_of_Video_leva = price_of_Video_Dollar * 1.57
price_of_RAM_Dollar = float(input())
ammount_of_RAM = int(input())
price_of_RAM_leva = ammount_of_RAM * price_of_RAM_Dollar * 1.57
discount_percent = float(input())

total = price_of_RAM_leva + (price_of_CPU_leva - ( price_of_CPU_leva * discount_percent)) + (price_of_Video_leva - (price_of_Video_leva* discount_percent))
print(price_of_RAM_leva)
print(price_of_CPU_leva)
print(price_of_Video_leva)

print(f"Money needed - {total:.2f} leva.")