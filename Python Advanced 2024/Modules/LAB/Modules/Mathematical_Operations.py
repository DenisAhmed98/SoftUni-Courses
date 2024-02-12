def math_operation(operation):
    n_one, sign, n_two = operation.split()

    if sign == "*":
        print(f"{float(n_one) * int(n_two):.2f}")
    elif sign == "/":
        print(f"{float(n_one) / int(n_two):.2f}")
    elif sign == "-":
        print(f"{int(n_two) - float(n_one):.2f}")
    elif sign == "+":
        print(f"{float(n_one) + int(n_two):.2f}")
    if sign == "^":
        print(f"{float(n_one) ** int(n_two):.2f}")