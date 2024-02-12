def fibonacci_Sequence(command):
    sequence = 0
    while True:
        command_list = command.split()
        count = 0
        num1 = 0
        num2 = 1
        next_number = num1

        if command_list[0] == "Create":
            sequence = int(command_list[2])
            count = 1
            num1 = 0
            num2 = 1
            next_number = num1
            while count <= sequence:
                print(next_number, end=" ")
                count += 1
                num1, num2 = num2, next_number
                next_number = num1 + num2

        elif command_list[0] == "Locate":
            flag = False
            index = 0
            count = 0
            num1 = 0
            num2 = 1
            next_number = num1
            while count <= sequence:
                if next_number == int(command_list[1]):
                    flag = True
                    index = count

                count += 1
                num1, num2 = num2, next_number
                next_number = num1 + num2
            if flag:
                print(f"The number - {command_list[1]} is at index {index}")
            else:
                print(f"The number {command_list[1]} is not in the sequence")

        elif command_list[0] == "Stop":
            break

        command = input()