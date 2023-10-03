hours = int(input())
day = input()

if (9 < hours < 19) and (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"):
    print("open")
else:
    print("closed")
