num_orders = int(input())
total_price = 0
for i in range (num_orders):
    ppc = float(input())
    days = int(input())
    cpd = int(input())
    if ppc < 0.01 or ppc > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif cpd < 1 or cpd > 2000:
        continue
    else:
        total_price = total_price + (ppc*days*cpd)
        print(f"The price for the coffee is: ${ppc*days*cpd:.2f}")

print(f"Total: ${total_price:.2f}")