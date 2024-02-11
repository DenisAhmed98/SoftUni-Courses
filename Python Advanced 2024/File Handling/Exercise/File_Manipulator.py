import os

while True:
    command, *info = input().split("-")

    if command == "Create":
        created_file = open(f"Files\{info[0]}", 'w')
        created_file.close()

    elif command == "Add":
        with open(f"Files\{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(f"Files\{info[0]}", "r+") as file:
                text = file.read()
                text = text.replace(info[1],info[2])
                file.seek(0)
                file.write(text)
                file.truncate()
        except FileNotFoundError:
            print("File was not found!")

    elif command == "Delete":
        try:
           os.remove(f"Files\{info[0]}")
        except FileNotFoundError:
            print("File was not found!")

    elif command == "End":
        break