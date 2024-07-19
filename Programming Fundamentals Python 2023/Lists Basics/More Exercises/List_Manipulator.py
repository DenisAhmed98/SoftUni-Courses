list_of_numbers = list(map(int, input().split(" ")))
command = input().split()
temp_list = []

while command[0] != "end":
    if command[0] == "exchange":
        if int(command[1]) > len(list_of_numbers) or int(command[1]) < 0:
            print("Invalid index")
        else:
            index = int(command[1]) + 1
            while len(list_of_numbers) > 0:
                if index >= len(list_of_numbers):
                    index = 0
                else:
                    temp_list.append(list_of_numbers[index])
                    list_of_numbers.pop(index)
            list_of_numbers = temp_list

    if command[0] == "max":
        flag = False
        max_index = 0
        index = 0
        r_index = 0
        if command[1] == "even":
            for x in list_of_numbers:
                if x % 2 == 0:
                    flag = True
                    if x>=max_index:
                        max_index = x
                        r_index = index
                index +=1
            if flag:
                print(r_index)
            else:
                print("No matches")

        elif command[1] == "odd":
            for x in list_of_numbers:
                if x % 2 == 1:
                    flag = True
                    if x >= max_index:
                        max_index = x
                        r_index = index
                index += 1
            if flag:
                print(r_index)
            else:
                print("No matches")

    if command[0] == "min":
        flag = False
        max_index = 10000
        index = 0
        r_index = 0
        if command[1] == "even":
            for x in list_of_numbers:
                if x % 2 == 0:
                    flag = True
                    if x<=max_index:
                        max_index = x
                        r_index = index
                index +=1
            if flag:
                print(r_index)
            else:
                print("No matches")

        elif command[1] == "odd":
            for x in list_of_numbers:
                if x % 2 == 1:
                    flag = True
                    if x <= max_index:
                        max_index = x
                        r_index = index
                index += 1
            if flag:
                print(r_index)
            else:
                print("No matches")

    if command[0] == "first":
        count = int(command[1])
        temp_list = []
        if count > len(list_of_numbers):
            print("Invalid count")
        elif command[2] == "even":
            for x in list_of_numbers:
                if x % 2 == 0:
                    temp_list.append(x)
                    count -=1
                if count == 0:
                    break
            print(temp_list)
        elif command[2] == "odd":
            for x in list_of_numbers:
                if x % 2 == 1:
                    temp_list.append(x)
                    count -=1
                if count == 0:
                    break
            print(temp_list)

    if command[0] == "last":
        count = int(command[1])
        temp_list = []
        if count > len(list_of_numbers):
            print("Invalid count")
        elif command[2] == "even":
            for x in list_of_numbers:
                if x % 2 == 0:
                    temp_list.append(x)
            while len(temp_list) > count:
                temp_list.pop(0)
            print(temp_list)
        elif command[2] == "odd":
            for x in list_of_numbers:
                if x % 2 == 1:
                    temp_list.append(x)
            while len(temp_list) > count:
                temp_list.pop(0)
            print(temp_list)

    command = input().split()

print(list_of_numbers)

