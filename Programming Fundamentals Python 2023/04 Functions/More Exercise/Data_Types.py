def data_Type(command,data):

    if command == "int":
        result = f"{2 * float(data):.0f}"
    elif command == "real":
        result = f"{1.5 * float(data):.2f}"
    elif command == "string":
        result = f"${data}$"

    return  result

command = input()
data = input()

print(data_Type(command,data))
